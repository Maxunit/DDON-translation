"""Prepare and merge local DDON translation chunks using the existing GMD overlays."""
import argparse
from collections import defaultdict
import csv
import fcntl
from fnmatch import fnmatchcase
import json
from pathlib import Path
import re
import tempfile

from build_gmd import TAGS, digest, is_data


PROTECTED = re.compile(TAGS.pattern + r'|\r\n|\r|\n')
MARKER = re.compile(r'\[\[DDON_(?:EN|JP)_\d+\]\]')
LANGUAGES = {'source_en': 'EN', 'source_jp': 'JP'}
ROOT = Path(__file__).resolve().parents[1]


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def snapshot(base):
    stat = base.stat()
    return [stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns]


def identity(group, entry):
    return (entry['key'], group['gmd_path'], group['arc_path'], str(entry['read_index']))


def mask(text, language):
    if '[[DDON_' in text:
        raise ValueError('Reserved placeholder prefix in source text')
    protected = []

    def replace(match):
        protected.append(match.group())
        return f'[[DDON_{language}_{len(protected)}]]'

    return PROTECTED.sub(replace, text), protected


def working_copy(source):
    entries = []
    for entry in source['entries']:
        refs = [
            {field: mask(variant[field], lang)[0] for field, lang in LANGUAGES.items()}
            for variant in (entry, *entry.get('alternate_sources', []))
        ]
        entries.append({
            'key': entry['key'], 'read_index': entry['read_index'],
            'tag_source': entry['tag_source'], **refs[0],
            **({'alternate_sources': refs[1:]} if refs[1:] else {}),
            'target_de': None,
        })
    return {field: source[field] for field in ('gmd_path', 'arc_path')} | {'entries': entries}


def restore(target, entry):
    field = entry['tag_source']
    masked, protected = mask(entry[field], LANGUAGES[field])
    if not isinstance(target, str) or not target.strip() or '\x00' in target:
        raise ValueError(f"{entry['key']}: target_de must be a nonblank string or null")
    if MARKER.findall(target) != MARKER.findall(masked):
        raise ValueError(f"{entry['key']}: missing, extra or reordered placeholders")
    if PROTECTED.search(target) or '[[DDON_' in MARKER.sub('', target):
        raise ValueError(f"{entry['key']}: raw control tags, line breaks or malformed placeholders")
    values = iter(protected)
    restored = MARKER.sub(lambda _: next(values), target)
    if PROTECTED.findall(restored) != protected:
        raise ValueError(f"{entry['key']}: restored controls differ from the source")
    return restored


def overlay_index(root):
    index = {}
    for path in sorted((root / 'German/translations').glob('*.json')):
        group = load(path)
        for entry in group['entries']:
            key = identity(group, entry)
            if key in index:
                raise ValueError(f'Duplicate translation identity: {key!r}')
            index[key] = path
    return index


def translation_candidates(root, pattern):
    base = root / 'gmd.csv'
    frozen = snapshot(base)
    covered = overlay_index(root)
    grouped = defaultdict(list)
    with base.open(encoding='utf-8', newline='') as stream:
        for row in csv.reader(stream, strict=True):
            if not is_data(row):
                continue
            if len(row) < 8 or not row[0].isdigit():
                raise ValueError('Invalid GMD data record')
            key = (row[1], row[4], row[5], row[7])
            matches = any(fnmatchcase(value.replace('\\', '/').casefold(), pattern) for value in key[:3])
            if key not in covered and matches:
                grouped[key].append({'source_jp': row[2], 'source_en': row[3]})
    if snapshot(base) != frozen:
        raise ValueError('GMD source changed during split')
    return frozen, grouped


def prepare(root, destination, rows, chars, pattern):
    if destination.exists():
        raise ValueError(f'Chunk directory already exists: {destination}')
    frozen, candidates = translation_candidates(root, pattern.replace('\\', '/').casefold())
    groups = defaultdict(list)
    review = []
    empty = 0
    for (key, gmd, arc, index), variants in candidates.items():
        if not any(PROTECTED.sub('', text).strip() for row in variants for text in row.values()):
            empty += 1
            continue
        if len({(v['source_jp'], v['source_en']) for v in variants}) != len(variants):
            review.append([key, gmd, arc, index, 'duplicate source rows'])
            continue
        tag_source = next(
            (field for field in LANGUAGES
             if PROTECTED.sub('', variants[0][field]).strip()
             and all(TAGS.findall(v[field]) == TAGS.findall(variants[0][field]) for v in variants)),
            None,
        )
        if tag_source is None:
            review.append([key, gmd, arc, index, 'incompatible source variants'])
            continue
        entry = {'key': key, 'read_index': index, 'tag_source': tag_source, **variants[0]}
        if len(variants) > 1:
            entry['alternate_sources'] = variants[1:]
        size = sum(len(value) for v in variants for value in v.values())
        groups[gmd, arc].append((entry, size))

    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination.parent) as temp:
        staged = Path(temp) / 'plan'
        (staged / 'sources').mkdir(parents=True)
        (staged / 'chunks').mkdir()
        manifest = {'schema_version': 1, 'base_snapshot': frozen, 'match': pattern,
                    'empty_or_control_only': empty, 'manual_review': review, 'chunks': {}}

        def write(gmd, arc, entries):
            name = f"chunk-{len(manifest['chunks']) + 1:05}.json"
            source = {'gmd_path': gmd, 'arc_path': arc, 'entries': entries}
            data = json_bytes(source)
            (staged / 'sources' / name).write_bytes(data)
            (staged / 'chunks' / name).write_bytes(json_bytes(working_copy(source)))
            manifest['chunks'][name] = {'sha256': digest(data), 'entries': len(entries),
                                        'gmd_path': gmd, 'arc_path': arc}

        for (gmd, arc), pending in groups.items():
            batch, length = [], 0
            for entry, size in pending:
                if batch and (len(batch) >= rows or length + size > chars):
                    write(gmd, arc, batch)
                    batch, length = [], 0
                batch.append(entry)
                length += size
            if batch:
                write(gmd, arc, batch)
        (staged / 'manifest.json').write_bytes(json_bytes(manifest))
        staged.rename(destination)
    count = sum(chunk['entries'] for chunk in manifest['chunks'].values())
    print(f'{count:,} entries in {len(manifest["chunks"]):,} chunks; '
          f'{len(review)} for manual review, {empty:,} empty/control-only')


def merge(root, draft_path):
    plan = draft_path.parent.parent
    manifest = load(plan / 'manifest.json')
    name = draft_path.name
    if manifest['schema_version'] != 1 or draft_path.parent.name != 'chunks' or name not in manifest['chunks']:
        raise ValueError('Expected a registered draft under the plan’s chunks directory')
    data = (plan / 'sources' / name).read_bytes()
    source_hash = digest(data)
    if source_hash != manifest['chunks'][name]['sha256']:
        raise ValueError(f'{name}: immutable sources changed')
    source = json.loads(data)
    expected = working_copy(source)
    draft = load(draft_path)
    texts = [entry.pop('target_de') for entry in draft['entries']]
    for entry in expected['entries']:
        del entry['target_de']
    if draft != expected:
        raise ValueError(f'{name}: only target_de may be edited')
    translated = []
    for entry, target in zip(source['entries'], texts, strict=True):
        if target is not None:
            translated.append(entry | {'text': restore(target, entry)})
    if not translated:
        print(f'{name}: no translations ready')
        return
    group = source | {'schema_version': 1, 'scope': 'DDON Chunk Manager', 'entries': translated}
    destination = root / 'German/translations' / f'chunk-{source_hash}.json'
    with (root / '.git/ddon-chunk-manager.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        if snapshot(root / 'gmd.csv') != manifest['base_snapshot']:
            raise ValueError('GMD source changed; prepare a fresh plan before merging')
        occupied = overlay_index(root)
        for entry in translated:
            key = identity(group, entry)
            if key in occupied and occupied[key] != destination:
                raise ValueError(f'{entry["key"]}: already translated in {occupied[key].name}')
        if destination.exists():
            previous = load(destination)
            if not all(entry in translated for entry in previous['entries']):
                raise ValueError('The draft removes or changes previously merged entries')
            if previous == group:
                print(f'{name}: already merged')
                return
        with tempfile.TemporaryDirectory(dir=destination.parent) as temp:
            staged = Path(temp) / destination.name
            staged.write_bytes(json_bytes(group))
            staged.replace(destination)
    print(f'{name}: {len(translated)} translations in {destination.relative_to(root)}')


def positive(value):
    number = int(value)
    if number < 1:
        raise argparse.ArgumentTypeError('must be greater than zero')
    return number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Path to the DDON checkout')
    commands = parser.add_subparsers(dest='command', required=True)
    split = commands.add_parser('split', help='Index source records and prepare masked drafts')
    split.add_argument('directory', type=Path)
    split.add_argument('--rows', type=positive, default=60, help='Maximum identities per chunk')
    split.add_argument('--chars', type=positive, default=10000,
                       help='Target maximum source characters; longer entries get their own chunk')
    split.add_argument('--match', default='*', help='Case-insensitive glob for key, GMD or ARC path')
    combine = commands.add_parser('merge', help='Validate and import filled targets in one draft')
    combine.add_argument('chunk', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'split':
            prepare(args.root.resolve(), args.directory.resolve(), args.rows, args.chars, args.match)
        else:
            merge(args.root.resolve(), args.chunk.resolve())
    except (OSError, ValueError, KeyError, TypeError, AttributeError, csv.Error) as error:
        parser.exit(1, f'{parser.prog}: {error}\n')


if __name__ == '__main__':
    main()

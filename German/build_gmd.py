"""Build the complete launcher CSV, preserving bytes outside translated MsgEn fields."""
import argparse
import csv
from collections import Counter
import hashlib
import io
import json
from itertools import zip_longest
from pathlib import Path, PureWindowsPath
import re

RAW_URL = 'https://raw.githubusercontent.com/Maxunit/DDON-translation/refs/heads/test/charselect-de-0.1.1/German/gmd.csv'
TAGS = re.compile(r'<[^>]*>')


def records(data):
    stream = io.BytesIO(data)
    lines = (line.decode('utf-8') for line in stream)
    start = 0
    for row in csv.reader(lines, strict=True):
        end = stream.tell()
        yield row, start, end
        start = end


def is_data(row):
    return bool(row and any(row) and not row[0].lstrip('\ufeff').startswith('#Index'))


def field_span(record, wanted):
    start = 0
    field = 0
    quoted = False
    i = 0
    while i < len(record):
        ch = record[i]
        if ch == 34 and (quoted or i == start):
            if quoted and i + 1 < len(record) and record[i + 1] == 34:
                i += 2
                continue
            quoted = not quoted
        elif not quoted and ch in (44, 13, 10):
            if field == wanted:
                return start, i
            if ch != 44:
                break
            field += 1
            start = i + 1
        i += 1
    if quoted:
        raise ValueError('Unclosed quoted field')
    if field == wanted:
        return start, len(record)
    raise ValueError('Missing CSV field')


def encode_field(value):
    stream = io.StringIO(newline='')
    csv.writer(stream, lineterminator='\r\n').writerow([value])
    return stream.getvalue()[:-2].encode('utf-8')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def render(base, groups, minimum=131125):
    targets = {}
    for group in groups:
        for entry in group['entries']:
            identity = (entry['key'], group['gmd_path'], group['arc_path'], str(entry['read_index']))
            if identity in targets:
                raise ValueError('Duplicate translation: ' + repr(identity))
            targets[identity] = entry
    if not targets:
        raise ValueError('No translations supplied')
    sources = {
        identity: Counter((source['source_jp'], source['source_en'])
                          for source in (entry, *entry.get('alternate_sources', [])))
        for identity, entry in targets.items()
    }
    found = {identity: Counter() for identity in targets}
    edits = []
    count = 0
    changed = 0
    for row, start, end in records(base):
        if not is_data(row):
            continue
        if len(row) < 8 or not row[0].isdigit():
            raise ValueError('Invalid source data record')
        count += 1
        identity = (row[1], row[4], row[5], row[7])
        if identity not in targets:
            continue
        source_pair = (row[2], row[3])
        expected_count = sources[identity][source_pair]
        if not expected_count:
            raise ValueError('Source text changed; review translation: ' + row[1])
        found[identity][source_pair] += 1
        if found[identity][source_pair] > expected_count:
            raise ValueError('Duplicate source entry: ' + repr(identity))
        entry = targets[identity]
        value = entry['text']
        if not isinstance(value, str) or '\x00' in value:
            raise ValueError('Invalid translation: ' + row[1])
        tag_source = entry.get('tag_source', 'source_en')
        if tag_source not in ('source_en', 'source_jp'):
            raise ValueError('Invalid tag source: ' + row[1])
        if TAGS.findall(value) != TAGS.findall(row[2 if tag_source == 'source_jp' else 3]):
            raise ValueError('Changed control tags: ' + row[1])
        if value == row[3]:
            continue
        a, b = field_span(base[start:end], 3)
        edits.append((start + a, start + b, encode_field(value)))
        changed += 1
    if count < minimum:
        raise ValueError(f'Incomplete base CSV: {count} records, minimum {minimum}')
    missing = {identity for identity, expected in sources.items() if found[identity] != expected}
    if missing:
        raise ValueError('Missing source entries: ' + repr(missing))
    pieces = []
    cursor = 0
    for a, b, replacement in edits:
        pieces.extend((base[cursor:a], replacement))
        cursor = b
    pieces.append(base[cursor:])
    result = b''.join(pieces)
    # Independently parse the full output; catch quoting/encoding and scope errors.
    for before, after in zip_longest(records(base), records(result)):
        if before is None or after is None:
            raise ValueError('Output record count changed')
        old, new = before[0], after[0]
        if old == new:
            continue
        identity = (old[1], old[4], old[5], old[7])
        if identity not in targets or old[:3] != new[:3] or old[4:] != new[4:]:
            raise ValueError('Unexpected change outside a translated MsgEn field')
        if new[3] != targets[identity]['text']:
            raise ValueError('Translation did not survive CSV encoding')
    return result, dict(data_records=count, covered_entries=len(found), changed_MsgEn_fields=changed)


def apply_supplement(root, base, output):
    """Add proven client keys that are absent from the pinned export."""
    path = root / 'German/gmd-supplement.json'
    if not path.is_file():
        return output, {}
    supplemental = json.loads(path.read_text(encoding='utf-8'))
    if supplemental['schema_version'] != 1 or supplemental['source_sha256'] != digest(base):
        raise ValueError('Supplemental GMD records require the pinned source CSV')
    occupied = {(row[4], row[5], row[7])
                for row, _, _ in records(output) if is_data(row)}
    rows = []
    for entry in supplemental['entries']:
        key, gmd, arc, index = (entry[field] for field in ('key', 'gmd_path', 'arc_path', 'read_index'))
        if not key or not index.isascii() or not index.isdecimal() or (gmd, arc, index) in occupied:
            raise ValueError(f'Invalid or occupied supplemental GMD slot: {(key, gmd, arc, index)!r}')
        text = entry['text']
        if not text.strip() or '\x00' in text or TAGS.findall(text) != TAGS.findall(entry['source_text']):
            raise ValueError(f'Invalid supplemental string: {key}')
        occupied.add((gmd, arc, index))
        rows.append([index, key, '', text, gmd, arc, PureWindowsPath(arc).name, index])
    with io.StringIO(newline='') as stream:
        csv.writer(stream, lineterminator='\r\n').writerows(rows)
        addition = stream.getvalue().encode('utf-8')
    if [row for row, _, _ in records(addition)] != rows:
        raise ValueError('Supplemental records did not survive CSV encoding')
    separator = b'' if output.endswith(b'\n') else b'\r\n'
    return output + separator + addition, {
        'added_records': len(rows),
        'supplemental_path': path.relative_to(root).as_posix(),
        'supplemental_sha256': digest(path.read_bytes()),
    }


def build(root):
    paths = sorted((root / 'German/translations').glob('*.json'))
    groups = [json.loads(p.read_text(encoding='utf-8')) for p in paths]
    base = (root / 'gmd.csv').read_bytes()
    output, stats = render(base, groups)
    output, extra = apply_supplement(root, base, output)
    stats['data_records'] += extra.get('added_records', 0)
    stats['covered_entries'] += extra.get('added_records', 0)
    manifest = dict(schema_version=1, description='Complete English base with German translation overlays',
                    source_path='gmd.csv', source_sha256=digest(base), raw_url=RAW_URL,
                    bytes=len(output), sha256=digest(output), **stats, **extra,
                    translation_files={p.relative_to(root).as_posix(): digest(p.read_bytes()) for p in paths})
    return {'German/gmd.csv': output,
            'German/gmd-manifest.json': (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Verify checked-in generated files without writing')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    files = build(root)
    for name, data in files.items():
        path = root / name
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                raise SystemExit('Generated file is out of date: ' + name)
        else:
            path.write_bytes(data)
    print(files['German/gmd-manifest.json'].decode('utf-8'))


if __name__ == '__main__':
    main()

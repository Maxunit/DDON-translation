"""Build the complete launcher CSV, preserving bytes outside translated MsgEn fields."""
import argparse
import csv
import hashlib
import io
import json
from itertools import zip_longest
from pathlib import Path
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
    found = set()
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
        if identity in found:
            raise ValueError('Duplicate source entry: ' + repr(identity))
        found.add(identity)
        entry = targets[identity]
        if row[2] != entry['source_jp'] or row[3] != entry['source_en']:
            raise ValueError('Source text changed; review translation: ' + row[1])
        value = entry['text']
        if not isinstance(value, str) or '\x00' in value:
            raise ValueError('Invalid translation: ' + row[1])
        tag_source = entry.get('tag_source', 'source_en')
        if tag_source not in ('source_en', 'source_jp'):
            raise ValueError('Invalid tag source: ' + row[1])
        if TAGS.findall(value) != TAGS.findall(entry[tag_source]):
            raise ValueError('Changed control tags: ' + row[1])
        if value == row[3]:
            continue
        a, b = field_span(base[start:end], 3)
        edits.append((start + a, start + b, encode_field(value)))
        changed += 1
    if count < minimum:
        raise ValueError(f'Incomplete base CSV: {count} records, minimum {minimum}')
    if found != targets.keys():
        raise ValueError('Missing source entries: ' + repr(targets.keys() - found))
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


def build(root):
    paths = sorted((root / 'German/translations').glob('*.json'))
    groups = [json.loads(p.read_text(encoding='utf-8')) for p in paths]
    base = (root / 'gmd.csv').read_bytes()
    output, stats = render(base, groups)
    manifest = dict(schema_version=1, description='Complete English base with German translation overlays',
                    source_path='gmd.csv', source_sha256=digest(base), raw_url=RAW_URL,
                    bytes=len(output), sha256=digest(output), **stats,
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

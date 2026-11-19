"""Reproduce the verified German ESC tab archive from the matching input."""

import argparse
import base64
import hashlib
import json
from pathlib import Path


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def apply_patch(source, patch):
    if len(source) != patch['size'] or sha256(source) != patch['source_sha256']:
        raise ValueError('Die Prüfsumme der Ausgangsdatei passt nicht zu diesem Patch.')
    archive = bytearray(source)
    previous_end = 0
    for offset, encoded in patch['changes']:
        change = base64.b64decode(encoded, validate=True)
        end = offset + len(change)
        if not change or offset < previous_end or end > len(archive):
            raise ValueError('Der Patch enthält einen ungültigen Dateibereich.')
        archive[offset:end] = change
        previous_end = end
    if sha256(archive) != patch['output_sha256']:
        raise ValueError('Die Prüfsumme des Ergebnisses stimmt nicht überein.')
    return bytes(archive)


def main():
    parser = argparse.ArgumentParser(description='Deutsche ESC-Reiter in eine separate ARC-Datei schreiben.')
    parser.add_argument('source', type=Path, help='Passende englische ddo_common.arc')
    parser.add_argument('output', type=Path, help='Neue ARC-Datei')
    args = parser.parse_args()
    try:
        patch = json.loads(Path(__file__).with_name('esc-tabs.patch.json').read_bytes())
        archive = apply_patch(args.source.read_bytes(), patch)
        with args.output.open('xb') as stream:
            stream.write(archive)
    except (OSError, ValueError) as error:
        parser.exit(1, f'{error}\n')
    print(f'Geprüfte Datei erstellt: {args.output}')


if __name__ == '__main__':
    main()

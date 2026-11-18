import copy
import csv
import importlib.util
import io
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('build_gmd', Path(__file__).resolve().parents[1] / 'build_gmd.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.row = ['1', 'key', '日本語\r\n二行目', 'Hello <VAL>', 'ui\\test.gmd', '\\ui\\test.arc', 'test.arc', '9', 'extra', '']
        self.entry = dict(key='key', read_index='9', source_jp=self.row[2], source_en=self.row[3], text='Grüße, "Welt"\r\n<VAL>')
        self.groups = [dict(gmd_path=self.row[4], arc_path=self.row[5], entries=[self.entry])]
        stream = io.StringIO(newline='')
        csv.writer(stream).writerow(self.row)
        self.record = stream.getvalue().encode('utf-8')
        # Preserve a BOM, repeated header, untouched unusual quoting, and extra columns.
        self.prefix = b'\xef\xbb\xbf#Index,Key,MsgJp,MsgEn,GmdPath,ArcPath,ArcName,ReadIndex\r\n'
        self.suffix = b'2,other,jp,"unchanged",ui\\other.gmd,\\ui\\other.arc,other.arc,0,,\r\n#Index,Key,MsgJp,MsgEn,GmdPath,ArcPath,ArcName,ReadIndex\r\n'
        self.base = self.prefix + self.record + self.suffix

    def render(self, base=None, groups=None, minimum=2):
        return builder.render(self.base if base is None else base, self.groups if groups is None else groups, minimum)

    def test_multiline_unicode_quoting_and_exact_untouched_bytes(self):
        result, stats = self.render()
        self.assertTrue(result.startswith(self.prefix))
        self.assertTrue(result.endswith(self.suffix))
        a, b = builder.field_span(self.record, 3)
        output_record = result[len(self.prefix):-len(self.suffix)]
        c, d = builder.field_span(output_record, 3)
        self.assertEqual(output_record[:c] + self.record[a:b] + output_record[d:], self.record)
        self.assertEqual(list(builder.records(result))[1][0][3], self.entry['text'])
        self.assertEqual(stats, dict(data_records=2, covered_entries=1, changed_MsgEn_fields=1))
        self.assertEqual(self.render()[0], result)

    def test_changed_english_or_japanese_requires_review(self):
        for column in ('source_en', 'source_jp'):
            groups = copy.deepcopy(self.groups)
            groups[0]['entries'][0][column] = 'changed'
            with self.assertRaisesRegex(ValueError, 'Source text changed'):
                self.render(groups=groups)

    def test_missing_and_duplicate_entries_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Missing source'):
            self.render(base=self.prefix + self.suffix, minimum=1)
        with self.assertRaisesRegex(ValueError, 'Duplicate source'):
            self.render(base=self.base + self.record)
        with self.assertRaisesRegex(ValueError, 'Duplicate translation'):
            self.render(groups=self.groups + self.groups)

    def test_missing_tags_and_partial_csv_are_rejected(self):
        groups = copy.deepcopy(self.groups)
        groups[0]['entries'][0]['text'] = 'Ohne Platzhalter'
        with self.assertRaisesRegex(ValueError, 'control tags'):
            self.render(groups=groups)
        with self.assertRaisesRegex(ValueError, 'Incomplete base'):
            self.render(minimum=131125)

    def test_explicit_japanese_tag_source_corrects_english_tag_error(self):
        row = self.row.copy()
        row[2] = 'JP <VAL>'
        row[3] = 'EN <VAL><VAL>'
        entry = dict(self.entry, source_jp=row[2], source_en=row[3])
        groups = [dict(self.groups[0], entries=[entry])]
        stream = io.StringIO(newline='')
        csv.writer(stream).writerow(row)
        base = self.prefix + stream.getvalue().encode('utf-8') + self.suffix
        with self.assertRaisesRegex(ValueError, 'control tags'):
            self.render(base=base, groups=groups)
        entry['tag_source'] = 'source_jp'
        result, _ = self.render(base=base, groups=groups)
        self.assertEqual(list(builder.records(result))[1][0][3], entry['text'])
        entry['tag_source'] = 'invalid'
        with self.assertRaisesRegex(ValueError, 'Invalid tag source'):
            self.render(base=base, groups=groups)

    def test_intentional_space_and_name_suffix_survive(self):
        for text in (' ', ' wird gelöscht.'):
            groups = copy.deepcopy(self.groups)
            groups[0]['entries'][0]['text'] = text + '<VAL>'
            result, _ = self.render(groups=groups)
            self.assertEqual(list(builder.records(result))[1][0][3], text + '<VAL>')


if __name__ == '__main__':
    unittest.main()

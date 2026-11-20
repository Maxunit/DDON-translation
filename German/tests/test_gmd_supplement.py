import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


spec = importlib.util.spec_from_file_location(
    "build_gmd", Path(__file__).resolve().parents[1] / "build_gmd.py"
)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class SupplementTests(unittest.TestCase):
    def setUp(self):
        tmp = TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.path = self.root / "German/gmd-supplement.json"
        self.path.parent.mkdir()
        self.base = b"0,original,jp,Hello,test.gmd,test.arc,test.arc,0"
        self.entry = dict(
            key="extra", gmd_path="test.gmd", arc_path="test.arc",
            read_index="1", source_text="English <VAL>", text='Grüße, "Welt" <VAL>',
        )

    def write_supplement(self, entries=None, source_hash=None):
        self.path.write_text(json.dumps(dict(
            schema_version=1,
            source_sha256=source_hash or builder.digest(self.base),
            entries=[self.entry] if entries is None else entries,
        )), encoding="utf-8")

    def test_append_to_csv_without_final_newline(self):
        self.write_supplement()
        output, stats = builder.apply_supplement(self.root, self.base, self.base)
        self.assertTrue(output.startswith(self.base + b"\r\n"))
        self.assertEqual([row for row, _, _ in builder.records(output)][1],
                         ["1", "extra", "", self.entry["text"], "test.gmd",
                          "test.arc", "test.arc", "1"])
        self.assertEqual(stats["added_records"], 1)

    def test_reject_occupied_slot_and_changed_base(self):
        self.write_supplement([dict(self.entry, read_index="0")])
        with self.assertRaisesRegex(ValueError, "occupied supplemental GMD slot"):
            builder.apply_supplement(self.root, self.base, self.base)
        self.write_supplement(source_hash="0" * 64)
        with self.assertRaisesRegex(ValueError, "pinned source CSV"):
            builder.apply_supplement(self.root, self.base, self.base)

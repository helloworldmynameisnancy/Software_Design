import unittest

from src.process_text import process_text

from src.blocks.uppercase_converter_block import convert as uppercase_converter
from src.blocks.lowercase_converter_block import convert as lowercase_converter
from src.blocks.z_blocker_block import convert as z_blocker
from src.blocks.upper_z_blocker_block import convert as Z_blocker

class ProcessTextTest(unittest.TestCase):
    def test_processor_text_with_no_blocks(self):
        self.assertEqual(process_text("a1B3Z4k!"), "a1B3Z4k!")

    def test_processor_text_with_upper_case_converter(self):
        self.assertEqual(process_text("a1B3Z4k!", uppercase_converter), "A1B3Z4K!")

    def test_processor_text_with_lower_case_converter(self):
        self.assertEqual(process_text("a1B3Z4k!", lowercase_converter), "a1b3z4k!")

    def test_processor_text_with_upper_case_and_lower_case_converter(self):
        self.assertEqual(process_text("a1B3Z4k!", uppercase_converter, lowercase_converter), "a1b3z4k!")

    def test_processor_text_with_upper_case_and_lower_case_converter_and_z_blocker(self):
        self.assertEqual(process_text("a1B3Z4k!", uppercase_converter, lowercase_converter, z_blocker), "a1b34k!")

    def test_processor_text_with_upper_case_and_lower_case_converter_and_Z_blocker(self):
        self.assertEqual(process_text("a1B3Z4k!", uppercase_converter, lowercase_converter, Z_blocker), "a1b3z4k!")

if __name__ == "__main__":
    unittest.main()

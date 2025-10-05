import unittest
from parameterized import parameterized

from src.blocks.lowercase_converter_block import convert

class LowerCaseConverterTest(unittest.TestCase):  
    @parameterized.expand(
        [
            ("A", "a"),
            ("a", "a"),
            ("1", "1"),
            (" ", " "),
        ]
    )
    def test_lower_case_converter_block(self, input, expected):
        self.assertEqual(convert(input), expected)

if __name__ == "__main__":
    unittest.main()

import unittest
from parameterized import parameterized

from src.blocks.multiplier_block import convert

class MultiplierTest(unittest.TestCase):  
    @parameterized.expand(
        [
            ("A", "AA"),
            ("a", "aa"),
            ("1", "11"),
            (" ", "  "),
        ]
    )
    def test_multiplier_block(self, input, expected):
        self.assertEqual(convert(input), expected)

if __name__ == "__main__":
    unittest.main()

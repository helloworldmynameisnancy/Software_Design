import unittest
from parameterized import parameterized

from src.get_perfect_numbers import get_factors, get_sum_of_factors, get_perfect_numbers, count_perfect_numbers


class GetPerfectNumbers(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand(
        [
            (1, [1]),
            (2, [1, 2]),
            (6, [1, 2, 3, 6]),
            (30, [1, 2, 3, 5, 6, 10, 15, 30]),
            (500, [1, 2, 4, 5, 10, 20, 25, 50, 100, 125, 250, 500])
        ]
    )
    def test_get_factors(self, number, expected_factors):
        self.assertEqual(get_factors(number), expected_factors)
    
    @parameterized.expand(
        [
            (1, 1),
            (2, 3),
            (6, 12),
            (30, 72),
            (500, 1092)
        ]
    )
    def test_get_sum_of_factors(self, number, expected_sum):
        self.assertEqual(get_sum_of_factors(number), expected_sum)
    
    @parameterized.expand(
        [
            (1, []),
            (2, []),
            (6, [6]),
            (30, [6, 28]),
            (500, [6, 28, 496])
        ]
    )
    def test_get_perfect_numbers(self, number, expected):
        self.assertEqual(get_perfect_numbers(number), expected)
    
    @parameterized.expand(
        [
            (1, 0),
            (2, 0),
            (6, 1),
            (30, 2),
            (500, 3)
        ]
    )
    def test_count_perfect_numbers(self, number, expected_count):
        self.assertEqual(count_perfect_numbers(number), expected_count)

if __name__ == "__main__":
    unittest.main()

from parameterized import parameterized

class BaseFactorial:
    def test_canary(self):
        self.assertTrue(True)

    @parameterized.expand(
        [
            (0, 1),
            (1, 1),
            (2, 2),
            (5, 120),
            (50, 30414093201713378043612608166064768844377641568960512000000000000),
        ]
    )
    def test_calculates_factorial_properly(self, input, expected):
        self.assertEqual(self.get_factorial_function()(input), expected)

    def test_raises_err_if_invalid_input_for_factorial(self):
        self.assertRaisesRegex(ValueError, "Factorials of negative numbers are undefined.", self.get_factorial_function(), -5)

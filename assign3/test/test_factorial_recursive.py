import unittest
from test_base_factorial import BaseFactorial
from src.factorial_recursive import factorial

class FactorialRecursive(unittest.TestCase, BaseFactorial):
    def get_factorial_function(self):
        return factorial

if __name__ == "__main__":
    unittest.main()

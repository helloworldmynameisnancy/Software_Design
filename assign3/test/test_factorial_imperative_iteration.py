import unittest
from test_base_factorial import BaseFactorial
from src.factorial_imperative_iteration import factorial

class FactorialImperativeIteration(unittest.TestCase, BaseFactorial):
    def get_factorial_function(self):
        return factorial

if __name__ == "__main__":
    unittest.main()

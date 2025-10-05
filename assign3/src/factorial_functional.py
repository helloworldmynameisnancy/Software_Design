from functools import reduce
from operator import mul as multiply
from .input_validator import input_validator

@input_validator
def factorial(number):
    return reduce(multiply, range(1, number + 1), 1)

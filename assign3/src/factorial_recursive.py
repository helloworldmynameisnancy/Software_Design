from .input_validator import input_validator

@input_validator
def factorial(number):
    return 1 if number < 2 else number * factorial(number - 1)

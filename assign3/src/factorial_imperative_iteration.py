from .input_validator import input_validator

@input_validator
def factorial(number):
    product = 1
    for i in range(1, number + 1):
        product *= i

    return product


def get_factors(number):
    return [i for i in range(1, number+1) if number % i == 0]

def get_sum_of_factors(number):
    return sum(get_factors(number))

def get_perfect_numbers(number):
    return [number for number in range(2, number + 1) if get_sum_of_factors(number) == number * 2]

def count_perfect_numbers(number):
    return len(get_perfect_numbers(number))

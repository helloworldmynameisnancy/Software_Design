from .get_perfect_numbers import count_perfect_numbers

def get_user_input():
    return int(input("Please enter a number greater than or equal to 1: "))

def output_perfect_numbers(number):
    number_of_perfect_numbers = count_perfect_numbers(number) 
    
    print(f"Here are the perfect numbers from 1 to {number}: {number_of_perfect_numbers}")

def main():
    number = get_user_input()
    
    output_perfect_numbers(number)

if __name__ == "__main__":
    main()

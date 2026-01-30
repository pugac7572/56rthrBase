"""# Simple command-line calculator
Base
This file provides a straightforward interactive calculator with the following operations:
- addition (+)
- subtraction (-)
- multiplication (*)
- division (/)
- integer division (//)
- modulo (%)
- power (**)

Usage:
Run the script and follow the menu prompts. Enter numbers (integers or floats). To exit, choose the "Quit" option.
"""

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def int_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Integer division by zero is not allowed")
    return a // b

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulo by zero is not allowed")
    return a % b

def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            value = input(prompt)
            # allow users to enter integers or floats
            if value.strip() == '':
                print("Empty input — please enter a number.")
                continue
            return float(value) if ('.' in value or 'e' in value.lower()) else int(value)
        except ValueError:
            print("Invalid number, please try again.")

def print_menu():
    print('\n=== Simple Calculator ===')
    print('1) Add (+)')
    print('2) Subtract (-)')
    print('3) Multiply (*)')
    print('4) Divide (/)')
    print('5) Integer divide (//)')
    print('6) Modulo (%)')
    print('7) Power (**)')
    print('8) Quit')

def main():
    while True:
        print_menu()
        choice = input('Choose an operation (1-8): ').strip()

        if choice == '8' or choice.lower() in ('q', 'quit', 'exit'):
            print('Goodbye!')
            break

        if choice not in [str(i) for i in range(1, 8)]:
            print('Unknown option, please choose a number between 1 and 8.')
            continue

        a = get_number('Enter the first number: ')
        b = get_number('Enter the second number: ')

        try:
            if choice == '1':
                result = add(a, b)
                op = '+'
            elif choice == '2':
                result = subtract(a, b)
                op = '-'
            elif choice == '3':
                result = multiply(a, b)
                op = '*'
            elif choice == '4':
                result = divide(a, b)
                op = '/'
            elif choice == '5':
                result = int_divide(a, b)
                op = '//$'
            elif choice == '6':
                result = modulo(a, b)
                op = '%'
            elif choice == '7':
                result = power(a, b)
                op = '**'

            print(f"\n{a} {op} {b} = {result}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == '__main__':
    main()

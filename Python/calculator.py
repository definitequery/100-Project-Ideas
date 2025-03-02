#!/usr/bin/python3
import sys
from typing import List

def print_help() -> None:
    """
    Prints the help message.
    
    Prints a help message with basic information about how to use this Python script.
    """
    help_message = f"""
    Basic Calculator
    Usage: python3 calculator.py <operation> <operand1> <operand2> [...]
    
    Operations:
      +   Addition (adds all operands)
      -   Subtraction (subtracts all subsequent operands from the first)
      x   Multiplication (multiplies all operands)
      /   Division (divides the first operand by each subsequent operand in order)
      %   Modulo (calculates the remainder when dividing the first operand by each subsequent operand in order)
    
    Example:
      python3 calculator.py + 5 3 2   # Outputs: 10
      python3 calculator.py / 10 2    # Outputs: 5.0
    
    Options:
      -h, --h, --help   Show this help message and exit
    """
    print(help_message)

def validate_number(value: str) -> int:
    """
    Validates and converts a string to an integer. If the conversion fails, prints the help message and exits.
    
    :param value: The string to convert.
    :return: The converted integer value.
    """
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number.")
        print_help()
        sys.exit(1)

def calculate(operation: str, numbers: List[int]) -> float:
    """
    Performs the specified mathematical operation on a list of numbers.
    
    :param operation: The mathematical operation ('+', '-', 'x', '/', '%').
    :param numbers: A list of integers to apply the operation on.
    :return: The result of the calculation as a float.
    """
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        return result
    elif operation == 'x':
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == '/':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Division by zero is not allowed.")
                print_help()
                sys.exit(1)
            result /= num
        return result
    elif operation == '%':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Modulo by zero is not allowed.")
                print_help()
                sys.exit(1)
            result %= num
        return result
    else:
        print("Unknown operation.")
        print_help()
        sys.exit(1)

if len(sys.argv) < 2:
    print("At least three arguments required (operation and two operands). Use --help for usage information.")
    print_help()
    sys.exit(1)

if sys.argv[1] in ('-h', '--h', '--help'):
    print_help()
    sys.exit(0)

operation: str = sys.argv[1]
numbers: List[str] = sys.argv[2:]
valid_operations = {'+', '-', 'x', '/', '%'}

if operation not in valid_operations:
    print(f"Invalid operation '{operation}'. Choose from {valid_operations}.")
    print_help()
    sys.exit(1)

numbers: List[int] = [validate_number(num) for num in numbers]
result: float = calculate(operation, numbers)
print(result)

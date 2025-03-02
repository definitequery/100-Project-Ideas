#!/usr/bin/python3
import sys
from typing import List

def print_help() -> None:
    """
    Display the help message.
    
    This function prints usage instructions for the calculator script,
    explaining the available operations and expected command-line arguments.
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
    Convert a string to an integer, exiting if the conversion fails.
    
    Args:
        value (str): The string to convert.
    
    Returns:
        int: The converted integer value.
    
    Exits:
        If the value cannot be converted to an integer, prints an error message
        and the help message, then exits the program.
    """
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid number.")
        print_help()
        sys.exit(1)

def calculate(operation: str, numbers: List[int]) -> float:
    """
    Perform a mathematical operation on a list of numbers.
    
    Args:
        operation (str): The mathematical operation ('+', '-', 'x', '/', '%').
        numbers (List[int]): A list of integers to apply the operation on.
    
    Returns:
        float: The result of the calculation.
    
    Exits:
        If division or modulo by zero occurs, prints an error message and exits.
        If an unknown operation is given, prints an error message and exits.
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
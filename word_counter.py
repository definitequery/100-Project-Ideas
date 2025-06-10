"""
Text Analysis Tool - Word Counter

This program analyzes text content by providing comprehensive statistics including
word count, character count (both with and without spaces), and line count.

The program can operate in two modes:
1. File mode: Pass a .txt file path as a command line argument
2. Interactive mode: Enter text directly when prompted

Input validation ensures only readable .txt files are processed, with clear
error messages for invalid files or permissions issues. Results are displayed
in a clean, organized format for easy reading.

Usage:
    python word_counter.py [file_path.txt]  # File mode
    python word_counter.py                  # Interactive mode
"""

from sys import argv
from os import path

def print_help():
    if len(argv) > 1:
        if argv[1] == '-h' or argv[1] == '--help':
            print(__doc__)
            exit(0)

def read_input():
    print_help()
    if len(argv) > 1:
        pathArg = path.abspath(argv[1])
        if path.splitext(pathArg)[1] != '.txt':
            raise ValueError(f'File at path #{pathArg} is not a text file')
        try:
            with open(pathArg, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            raise ValueError(f'File at path #{pathArg} does not exist')
        except PermissionError:
            raise ValueError(f'File at path #{pathArg} is not readable')
        except Exception as e:
            raise ValueError(f'Error reading file at path #{pathArg}: {e}')
    else:
        text = input('Enter a text or file path: ')
    return text

def word_count(text):
    return len(text.split())

def character_count(text, with_spaces=True):
    if with_spaces:
        return len(text)
    return len(text.replace(' ', ''))

def line_count(text):
    return text.count('\n') + 1

def print_results(text):
    print('\nResults:')
    print('--------')
    print(f'Words: {word_count(text)}')
    print(f'Characters (with spaces): {character_count(text)}')
    print(f'Characters (without spaces): {character_count(text, False)}')
    print(f'Lines: {line_count(text)}')

if __name__ == '__main__':
    print_results(read_input())
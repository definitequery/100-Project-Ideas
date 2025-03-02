#!/usr/bin/python3
from random import randint

answer = randint(1, 100)
number_of_guesses = 10

print("Welcome to the Number-Guessing Game")
print("I've chosen a number between 1 and 100. Try to guess what it is.")

def read_guess():
  """
  Continuously prompts the user to enter a guess until a valid integer is provided.

  Returns:
    int: The user's valid numerical guess.
  """
  while True:
    user_response = input('Enter a guess: ')
    try:
      guess = int(user_response)
      return guess
    except ValueError:
      print("Error: Input must be a number.")

def is_valid(number_to_check):
  """
  Checks if the given input can be converted to an integer.

  Args:
    number_to_check (str): The input value to validate.

  Returns:
    bool: True if the input is a valid integer, False otherwise.
  """
  try:
    int(number_to_check)
    return True
  except:
    return False

guess = read_guess()
while True:
  number_of_guesses -= 1
  if number_of_guesses == 0:
    print("You ran out of guesses. Better luck next time!")
    break

  if (guess == answer):
    print("You guessed correctly! Thanks for playing!")
    break

  if guess < answer:
    print(f"That guess is too low. Please try again")
  else:
    print(f"That guess is too high. Please try again.")
  guess = read_guess()
from random import randint

MAX_ATTEMPTS = 10

number = randint(1, 100)
attempts_remaining = MAX_ATTEMPTS

while attempts_remaining > 0:
  print(f'You have {attempts_remaining} attempt(s) remaining.')
  guess = int(input('I\'ve chosen a number between 1 and 100. Try to guess it: '))
  if guess < number:
    print('Too low!')
  elif guess > number:
    print('Too high!')
  else:
    print(f'You guessed it! The number was {number}. You found it in {MAX_ATTEMPTS - attempts_remaining} attempts.')
    break
  attempts_remaining -= 1

if attempts_remaining == 0:
  print(f'You didn\'t guess the number. The number was {number}.')
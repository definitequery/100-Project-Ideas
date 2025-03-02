#!/usr/bin/python3

def read_temperature() -> float:
  """
  Prompt the user to enter a temperature value and validate the input.
  
  This function continuously asks the user for a temperature value until a valid numerical input is provided.
  
  Returns:
    float: The valid temperature input from the user.
  """
  while True:
    user_response = input('Enter temperature to convert: ')
    try:
      temperature = float(user_response)
      return temperature
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

def select_mode() -> str:
  """
  Prompt the user to select a temperature conversion mode.
  
  The user must choose either 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius.
  The function keeps prompting until a valid choice is entered.
  
  Returns:
    str: The chosen conversion mode ('c' or 'f').
  """
  while True:
    mode = input('Choose conversion mode. Enter C to convert Celsius temperatures or F to convert Fahrenheit temperatures: ')
    if mode.lower() in ('c', 'f'):
      return mode.lower()
    print('Error: Invalid option. Please choose C or F.')

def convert_to_celsius(fahrenheit: float) -> float:
  """
  Convert a Fahrenheit temperature to Celsius.
  
  Args:
    fahrenheit (float): Temperature in Fahrenheit.
  
  Returns:
    float: Equivalent temperature in Celsius.
  """
  return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius: float) -> float:
  """
  Convert a Celsius temperature to Fahrenheit.
  
  Args:
    celsius (float): Temperature in Celsius.
  
  Returns:
    float: Equivalent temperature in Fahrenheit.
  """
  return celsius * 9 / 5 + 32

def convert_temperature() -> None:
  """
  Execute the temperature conversion process.
  
  This function prompts the user to select a conversion mode, reads a temperature value,
  performs the conversion, and prints the result.
  """
  print('\n' + '*' * 30)
  mode = select_mode()
  temperature = read_temperature()
  
  if mode == 'c':
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f'{temperature} degrees Celsius = {fahrenheit:.1f} degrees Fahrenheit')
  else:
    celsius = convert_to_celsius(temperature)
    print(f'{temperature} degrees Fahrenheit = {celsius:.1f} degrees Celsius')
  print('*' * 30 + '\n')

convert_temperature()
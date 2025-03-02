#!/usr/bin/python3

def select_mode() -> str:
  """Select temperature conversion mode.

  Set calculator conversion mode. Choosing C will convert Celsius temperatures to Fahrenheit and
  vice versa.
  """
  while True:
    mode = input('Choose conversion mode. Enter C to convert Celsius temperatures or F to convert Fahrenheit temperatures: ')
    if (mode.lower() == 'c' or mode.lower() == 'f'):
      break
    print('Error: Invalid option. Please choose C or F.')
  return mode

def convert_to_celsius(fahrenheit: float) -> float:
  """Convert Fahrenheit temperature to Celsius."""
  return (fahrenheit - 32) * 5 / 9;

def convert_to_fahrenheit(celsius: float) -> float:
  """Convert Celsius temperature to Fahrenheit."""
  return celsius * 9 / 5 + 32;

def convert_temperature() -> None:
  """Select mode, read temperature, and output conversion.

  After selecting a temperature mode, this function reads a floating-point temperature in that unit
  from the user and outputs the equivalent conversion.
  """
  print('\n' + '*' * 30)
  mode = select_mode()
  
  temperature_input = input(f'Enter {mode.upper()}° temperature to convert: ')
  try:
    temperature = float(temperature_input)
  except ValueError:
    print('Invalid temperature. Please enter a numeric value.')
    return
  
  if mode == 'c':
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f'{temperature} degrees Celsius = {fahrenheit:.1f} degrees Fahrenheit')
  else:
    celsius = convert_to_celsius(temperature)
    print(f'{temperature} degrees Fahrenheit = {celsius:.1f} degrees Celsius')
  print('*' * 30 + '\n')

convert_temperature()
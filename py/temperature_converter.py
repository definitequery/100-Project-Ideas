mode = input('What unit would you like to convert from? (F or C): ')
while mode.lower() not in ('f', 'c'):
  print('Invalid input. Please enter F or C.')
  mode = input('What unit would you like to convert from? (F or C): ')

if mode.lower() == 'f':
  temp = float(input('Enter the temperature in Fahrenheit: '))
  celsius = (temp - 32) * 5/9
  print(f'{temp}°F is {celsius:.2f}°C')
else:
  temp = float(input('Enter the temperature in Celsius: '))
  fahrenheit = (temp * 9/5) + 32
  print(f'{temp}°C is {fahrenheit:.2f}°F')
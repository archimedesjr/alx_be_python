FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temperature_to_convert = int(input("Enter the temperature to convert: "))
choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if choice == "F":
  def convert_to_celsius(temperature_to_convert):
    celsius = (temperature_to_convert - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(celsius)
  convert_to_celsius(temperature_to_convert)
elif choice == "C":
  def convert_to_fahrenheit(temperature_to_convert):
    fahrenheit = (temperature_to_convert * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(fahrenheit)
  convert_to_fahrenheit(temperature_to_convert)
else:
  print("Invalid temperature. Please enter a numeric value.")
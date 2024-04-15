# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage
celsius_temperature = 30
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print("Temperature in Fahrenheit:", fahrenheit_temperature)

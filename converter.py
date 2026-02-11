# Exercise A: The Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))

# Formula: F = (C * 1.8) + 32
fahrenheit = (celsius * 1.8) + 32

print(f"The temperature in Fahrenheit is: {fahrenheit}")

# Bonus Requirements
if celsius < 0:
    print("Freezing!")
elif celsius > 30:
    print("Hot!")

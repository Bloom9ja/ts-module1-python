fraction = input("Fraction: ")

try:
    numerator, denominator = fraction.split("/")
    fuel_percentage = int(numerator) / int(denominator) * 100
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    if fuel_percentage <= 1:
        print("E")
    elif fuel_percentage >= 99:
        print("F")
    else:
        print(f"{fuel_percentage}%")
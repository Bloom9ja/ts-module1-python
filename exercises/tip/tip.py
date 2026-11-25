# meal_cost = input("How much is the meal? -> $")
# tip_percentage = input("How many percent is the tip? -> ")

# dollars_to_float = float(meal_cost)
# percent_to_float = float(tip_percentage)

def dollars_to_float(value):
    value = value.replace("$", "")
    return float(value)

def percent_to_float(value):
    value = float(value.replace("%", "")) / 100
    return (value)

def main():
    meal_cost = input("How much is my meal? ")
    tip_percentage = input("How many percent is the tip? ")
    tip = dollars_to_float(meal_cost) * percent_to_float(tip_percentage)
    print(f"The tip is ${tip:.2f}")

main()
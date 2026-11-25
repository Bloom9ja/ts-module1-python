price = 50
remaining = price

while remaining > 0:
    amount_paid = int(input("Insert your coin: "))

    if amount_paid == 25 or amount_paid == 10 or amount_paid == 5:
        remaining = remaining - amount_paid

    print(f"Amount Due: {max(0, remaining)}")
print(f"Change Owed: {abs(remaining)}")
count = 0

with open("test.py", "r") as file:
    for line in file:
        if line.strip().startswith("#"):
            continue
        if not line.strip():
            continue
        count = count + 1

print(count)
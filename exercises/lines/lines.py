import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python lines.py filename.py")

count = 0

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.strip().startswith("#"):
                continue
            if not line.strip():
                continue
            count = count + 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count)
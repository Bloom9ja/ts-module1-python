import csv
from statistics import mean, median

# students = [
#     {"name": "Ada", "score": 91},
#     {"name": "Tolu", "score": 78},
#     {"name": "Chi", "score": 68},
#     {"name": "Bloom", "score": 90}
# ]

# with open("exercises/scores/scores.csv", "w", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "score"])
#     writer.writeheader()
#     writer.writerows(students)

students = []

with open("exercises/scores/scores.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

scores = []

for student in students:
    scores.append(int(student["score"]))

top_student = max(students, key = lambda student: int(student["score"]))
bottom_student = min(students, key = lambda student: int(student["score"]))

print(scores)
print(f"Mean: {mean(scores)}")
print(f"Median: {median(scores)}")
print(f"Top student: {top_student['name']} - {top_student['score']}")
print(f"Bottom student: {bottom_student['name']} - {bottom_student['score']}")
# CUL-CYB 371 - Assignment Two
# Create a fictional student dataset and save it as a CSV file.

import csv

students = [
    ["CUL001", "Computer Science", 100, 92, 78],
    ["CUL002", "Cyber Security", 200, 88, 84],
    ["CUL003", "Software Engineering", 300, 95, 91],
    ["CUL004", "Computer Science", 200, 76, 69],
    ["CUL005", "Information Technology", 100, 83, 74],
    ["CUL006", "Cyber Security", 300, 90, 88],
    ["CUL007", "Software Engineering", 400, 97, 93],
    ["CUL008", "Information Technology", 200, 68, 62],
    ["CUL009", "Computer Science", 300, 85, 81],
    ["CUL010", "Cyber Security", 100, 79, 72],
    ["CUL011", "Software Engineering", 200, 91, 86],
    ["CUL012", "Information Technology", 300, 87, 79],
    ["CUL013", "Computer Science", 400, 94, 89],
    ["CUL014", "Cyber Security", 200, 72, 67],
    ["CUL015", "Software Engineering", 100, 89, 82],
]

filename = "student_dataset.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Student ID",
        "Department",
        "Level",
        "Attendance Percentage",
        "Average Examination Score"
    ])
    writer.writerows(students)

print(f"Dataset created successfully: {filename}")

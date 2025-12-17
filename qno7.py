students = [
    {"name": "ram", "math_grade": 43},
    {"name": "hari", "math_grade": 65},
    {"name": "sita", "math_grade": 90}
]

for student in students:
    if student["math_grade"] >= 70:
        student["status"] = "Approved"
    else:
        student["status"] = "Rejected"

print(students)

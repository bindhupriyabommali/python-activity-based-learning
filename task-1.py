
# University Scholarship Allocation System

students = [
    {
        "name": "Ravi",
        "marks": 90,
        "subjects": [85, 90, 88],
        "attendance": 95,
        "income": 150000
    },
    {
        "name": "Priya",
        "marks": 95,
        "subjects": [92, 88, 95],
        "attendance": 98,
        "income": 100000
    },
    {
        "name": "Kiran",
        "marks": 80,
        "subjects": [75, 80, 78],
        "attendance": 85,
        "income": 200000
    },
    {
        "name": "Sneha",
        "marks": 90,
        "subjects": [90, 85, 88],
        "attendance": 95,
        "income": 120000
    }
]

# Scholarship eligibility criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARKS = 70
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

def check_eligibility(student):
    return (
        student["marks"] >= MIN_AGGREGATE
        and all(mark >= MIN_SUBJECT_MARKS
                for mark in student["subjects"])
        and student["attendance"] >= MIN_ATTENDANCE
        and student["income"] <= MAX_INCOME
    )

# Separate eligible and rejected students
eligible = []
rejected = []

for student in students:
    if check_eligibility(student):
        eligible.append(student)
    else:
        rejected.append(student)

# Ranking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
eligible.sort(
    key=lambda s: (
        -s["marks"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

# Display eligible students in rank order
print("UNIVERSITY SCHOLARSHIP RESULTS")
print("-" * 55)

if eligible:
    print("\nEligible Students:")
    for rank, student in enumerate(eligible, start=1):
        print(
            f"Rank {rank}: {student['name']} | "
            f"Marks: {student['marks']}% | "
            f"Attendance: {student['attendance']}% | "
            f"Income: Rs.{student['income']}"
        )
else:
    print("No students are eligible.")

# Display rejected students
print("\nNot Eligible Students:")
for student in rejected:
    print(student["name"])

# Allocate scholarships to the top 3 eligible students
SCHOLARSHIP_LIMIT = 3

print("\nScholarship Allocation:")
for student in eligible[:SCHOLARSHIP_LIMIT]:
    print(student["name"], "- Scholarship Approved")

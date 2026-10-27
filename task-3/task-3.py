
# Smart Campus Incident and Maintenance Prioritization

# Sample maintenance reports
reports = [
    {"id": 1, "issue": "Water Leakage", "severity": 4,
     "location": "Hostel", "frequency": 5},

    {"id": 2, "issue": "Broken Fan", "severity": 2,
     "location": "Classroom", "frequency": 3},

    {"id": 3, "issue": "Electrical Fault", "severity": 5,
     "location": "Laboratory", "frequency": 4},

    {"id": 4, "issue": "Damaged Road", "severity": 3,
     "location": "Campus Entrance", "frequency": 2},

    {"id": 5, "issue": "Blocked Drain", "severity": 3,
     "location": "Hostel", "frequency": 4}
]

# Location importance
location_priority = {
    "Laboratory": 5,
    "Hostel": 4,
    "Classroom": 3,
    "Campus Entrance": 3
}

# Calculate priority score
def calculate_priority(report):
    severity = report["severity"]
    frequency = report["frequency"]
    location = location_priority.get(report["location"], 1)

    score = (severity * 5) + (frequency * 2) + location

    return score

# Classify incidents
def classify(score):
    if score >= 30:
        return "CRITICAL"
    elif score >= 22:
        return "HIGH"
    elif score >= 15:
        return "MEDIUM"
    else:
        return "LOW"

# Calculate and classify every report
for report in reports:
    report["score"] = calculate_priority(report)
    report["priority"] = classify(report["score"])

# Sort reports by score (highest first)
reports.sort(key=lambda x: x["score"], reverse=True)

# Display ranked reports
print("SMART CAMPUS MAINTENANCE REPORT")
print("-" * 75)
print(f"{'Rank':<6}{'Issue':<20}{'Location':<20}"
      f"{'Score':<10}{'Priority'}")
print("-" * 75)

for rank, report in enumerate(reports, start=1):
    print(f"{rank:<6}{report['issue']:<20}"
          f"{report['location']:<20}"
          f"{report['score']:<10}{report['priority']}")

# Generate priority summary
print("\nPRIORITY SUMMARY")
print("-" * 30)

for level in ["CRITICAL", "HIGH", "MEDIUM", "LOW"]:
    count = sum(1 for r in reports if r["priority"] == level)
    print(f"{level}: {count} incident(s)")

print("\nHighest priority issue:")
if reports:
    print(reports[0]["issue"], "-", reports[0]["priority"])

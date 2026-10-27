
# Multi-Event Sports Scheduling and Scoring

# Event schedule using tuples
# Format: (Event Name, Team 1, Team 2, Start Time)

schedule = [
    ("Cricket", "Team A", "Team B", "10:00"),
    ("Football", "Team C", "Team D", "10:00"),
    ("Volleyball", "Team A", "Team C", "11:00"),
    ("Basketball", "Team B", "Team D", "12:00"),
    ("Badminton", "Team A", "Team D", "13:00")
]

# Team scores using a dictionary
scores = {
    "Team A": [10, 15, 20],
    "Team B": [20, 10, 15],
    "Team C": [15, 20, 10],
    "Team D": [10, 15, 20]
}

# 1. Display the schedule
print("SPORTS EVENT SCHEDULE")
for event in schedule:
    print(event)

# 2. Identify scheduling conflicts
print("\nSCHEDULING CONFLICTS")

conflict_found = False

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        event1 = schedule[i]
        event2 = schedule[j]

        if event1[3] == event2[3]:
            teams1 = {event1[1], event1[2]}
            teams2 = {event2[1], event2[2]}

            common_teams = teams1 & teams2

            if common_teams:
                print(
                    event1[0], "and", event2[0],
                    "have a conflict for",
                    ", ".join(sorted(common_teams)),
                    "at", event1[3]
                )
                conflict_found = True

if not conflict_found:
    print("No scheduling conflicts found.")

# 3. Calculate total points
print("\nTOTAL TEAM POINTS")

total_points = {}

for team, points in scores.items():
    total_points[team] = sum(points)
    print(team, ":", total_points[team], "points")

# 4. Generate final rankings
rankings = sorted(
    total_points.items(),
    key=lambda item: (-item[1], item[0])
)

print("\nFINAL TEAM RANKINGS")

for rank, (team, points) in enumerate(rankings, start=1):
    print(rank, ".", team, "-", points, "points")

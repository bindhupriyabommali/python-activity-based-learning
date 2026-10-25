
# Student Timetable Conflict Detection

# Course schedules stored as tuples:
# (course_name, day, start_time, end_time, room)

courses = [
    ("Python", "Monday", "09:00", "10:00", "R101"),
    ("Mathematics", "Monday", "09:30", "10:30", "R102"),
    ("Physics", "Tuesday", "10:00", "11:00", "R103"),
    ("Chemistry", "Monday", "11:00", "12:00", "R101")
]

# Rooms that are unavailable at specific times
unavailable_rooms = [
    ("R101", "Monday", "11:00", "12:00"),
    ("R103", "Tuesday", "10:00", "11:00")
]

# Convert time string to minutes
def time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

# Check whether two classes overlap
def has_conflict(course1, course2):
    if course1[1] != course2[1]:
        return False

    start1 = time_to_minutes(course1[2])
    end1 = time_to_minutes(course1[3])
    start2 = time_to_minutes(course2[2])
    end2 = time_to_minutes(course2[3])

    return start1 < end2 and start2 < end1

# Validate time inputs
def valid_time(start, end):
    try:
        start_minutes = time_to_minutes(start)
        end_minutes = time_to_minutes(end)

        return (
            len(start.split(":")) == 2
            and len(end.split(":")) == 2
            and 0 <= start_minutes < 1440
            and 0 <= end_minutes < 1440
            and start_minutes < end_minutes
        )
    except (ValueError, AttributeError):
        return False

# Check timetable
print("STUDENT TIMETABLE CONFLICT DETECTION")
print("-" * 45)

conflict_found = False

# Check for overlapping classes
for i in range(len(courses)):
    for j in range(i + 1, len(courses)):
        if has_conflict(courses[i], courses[j]):
            print(
                "Schedule Conflict:",
                courses[i][0], "and", courses[j][0]
            )
            conflict_found = True

if not conflict_found:
    print("No overlapping classes found.")

# Check unavailable rooms
print("\nUnavailable Room Check:")

room_conflict_found = False

for course in courses:
    for room in unavailable_rooms:
        if (
            course[4] == room[0]
            and course[1] == room[1]
            and time_to_minutes(course[2]) < time_to_minutes(room[3])
            and time_to_minutes(room[2]) < time_to_minutes(course[3])
        ):
            print(
                course[0], "cannot use room", course[4],
                "on", course[1]
            )
            room_conflict_found = True

if not room_conflict_found:
    print("All rooms are available.")

# Validate proposed timetable
print("\nTimetable Validation:")

valid = True

for course in courses:
    if not valid_time(course[2], course[3]):
        print("Invalid time for course:", course[0])
        valid = False

if not conflict_found and not room_conflict_found and valid:
    print("Timetable is VALID.")
else:
    print("Timetable is INVALID. Please correct the conflicts.")

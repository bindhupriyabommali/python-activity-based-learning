
# Student Timetable Conflict Detection

# Timetable format: (Course, Day, Start Time, End Time, Room)
timetable = [
    ("Python", "Monday", "09:00", "10:00", "R101"),
    ("Mathematics", "Monday", "09:30", "10:30", "R102"),
    ("Physics", "Monday", "10:00", "11:00", "R101"),
    ("Chemistry", "Tuesday", "09:00", "10:00", "R103"),
    ("English", "Monday", "11:00", "12:00", "R101")
]

# Rooms unavailable at specific times
unavailable_rooms = [
    ("R101", "Monday", "10:00", "11:00"),
    ("R103", "Tuesday", "09:00", "10:00")
]

def to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def overlaps(start1, end1, start2, end2):
    return (to_minutes(start1) < to_minutes(end2) and
            to_minutes(start2) < to_minutes(end1))

def validate_timetable(timetable):
    conflicts = []

    # Check overlapping courses and room clashes
    for i in range(len(timetable)):
        c1, d1, s1, e1, r1 = timetable[i]

        for j in range(i + 1, len(timetable)):
            c2, d2, s2, e2, r2 = timetable[j]

            if d1 == d2 and overlaps(s1, e1, s2, e2):
                if r1 == r2:
                    conflicts.append(
                        f"Room conflict: {c1} and {c2} "
                        f"both use {r1} at overlapping times."
                    )

                if c1 != c2:
                    conflicts.append(
                        f"Schedule overlap: {c1} and {c2} "
                        f"on {d1}."
                    )

    # Check room unavailability
    for course, day, start, end, room in timetable:
        for unavailable_room, unavailable_day, us, ue in unavailable_rooms:
            if room == unavailable_room and day == unavailable_day:
                if overlaps(start, end, us, ue):
                    conflicts.append(
                        f"Unavailable room: {room} for {course} "
                        f"on {day}, {start}-{end}."
                    )

    return conflicts

# Display timetable
print("STUDENT TIMETABLE")
print("-" * 55)

for course, day, start, end, room in timetable:
    print(f"{course:12} {day:10} {start}-{end}  Room: {room}")

# Validate timetable
print("\nTIMETABLE VALIDATION")
print("-" * 55)

conflicts = validate_timetable(timetable)

if conflicts:
    for conflict in conflicts:
        print("CONFLICT:", conflict)
else:
    print("Timetable is valid. No conflicts found.")

# Validate a proposed new course
proposed_course = ("Computer Networks", "Monday",
                   "11:30", "12:30", "R101")

print("\nPROPOSED COURSE:", proposed_course[0])

proposed_timetable = timetable + [proposed_course]
proposed_conflicts = validate_timetable(proposed_timetable)

if proposed_conflicts:
    print("Proposed timetable is NOT valid.")
    for conflict in proposed_conflicts:
        print("-", conflict)
else:
    print("Proposed timetable is valid.")

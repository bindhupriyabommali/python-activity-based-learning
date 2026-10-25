
from datetime import datetime, timedelta
import math

# Parking rates per hour
RATES = {
    "bike": 20,
    "car": 50,
    "truck": 80
}

DAILY_LIMIT = {
    "bike": 150,
    "car": 400,
    "truck": 600
}

PENALTY = 200


def calculate_parking_fee(entry, exit_time, vehicle):
    try:
        entry_time = datetime.strptime(entry, "%Y-%m-%d %H:%M")
        exit_datetime = datetime.strptime(exit_time, "%Y-%m-%d %H:%M")
    except ValueError:
        return "Error: Invalid date or time format."

    if vehicle not in RATES:
        return "Error: Invalid vehicle category."

    if exit_datetime <= entry_time:
        return "Error: Exit time must be after entry time."

    # Calculate total parking duration
    duration = exit_datetime - entry_time
    total_minutes = duration.total_seconds() / 60
    hours = math.ceil(total_minutes / 60)

    # Count calendar days covered by parking
    days = (exit_datetime.date() - entry_time.date()).days + 1

    # Calculate fee for each parking day
    total_fee = 0
    current_time = entry_time

    while current_time < exit_datetime:
        next_day = datetime.combine(
            current_time.date() + timedelta(days=1),
            datetime.min.time()
        )

        segment_end = min(next_day, exit_datetime)
        segment_minutes = (
            segment_end - current_time
        ).total_seconds() / 60

        segment_hours = math.ceil(segment_minutes / 60)

        daily_fee = min(
            segment_hours * RATES[vehicle],
            DAILY_LIMIT[vehicle]
        )

        total_fee += daily_fee
        current_time = segment_end

    # Overnight parking charge
    overnight_fee = 100 if days > 1 else 0

    # Penalty for parking over 24 hours
    penalty_fee = PENALTY if total_minutes > 24 * 60 else 0

    total = total_fee + overnight_fee + penalty_fee

    return {
        "Vehicle": vehicle.title(),
        "Parking Duration": f"{hours} hour(s)",
        "Base Parking Fee": f"Rs. {total_fee}",
        "Overnight Fee": f"Rs. {overnight_fee}",
        "Penalty": f"Rs. {penalty_fee}",
        "Total Fee": f"Rs. {total}"
    }


# Main program
print("=== SMART PARKING FEE MANAGEMENT ===")
print("Vehicle categories: bike, car, truck")

vehicle = input("Enter vehicle category: ").strip().lower()
entry = input("Enter entry time (YYYY-MM-DD HH:MM): ").strip()
exit_time = input("Enter exit time (YYYY-MM-DD HH:MM): ").strip()

result = calculate_parking_fee(entry, exit_time, vehicle)

if isinstance(result, dict):
    print("\n--- PARKING BILL ---")
    for key, value in result.items():
        print(f"{key}: {value}")
else:
    print(result)

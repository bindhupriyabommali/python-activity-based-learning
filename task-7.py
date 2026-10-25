
import math

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input event expenses
venue = float(input("Enter venue cost: ₹"))
equipment = float(input("Enter equipment cost: ₹"))
catering_per_person = float(input("Enter catering cost per participant: ₹"))
transport = float(input("Enter transport cost: ₹"))
certificate_per_person = float(input("Enter certificate cost per participant: ₹"))

# Input event details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: ₹"))
registration_fee = float(input("Enter registration fee per participant: ₹"))

# Validate inputs
if (min(venue, equipment, catering_per_person, transport,
        certificate_per_person, sponsorship, registration_fee) < 0
        or participants <= 0):
    print("Error: Costs and sponsorship must be non-negative,")
    print("participants must be positive.")
else:
    # Calculate expenses
    fixed_cost = venue + equipment + transport
    variable_cost = catering_per_person + certificate_per_person
    total_variable_cost = variable_cost * participants
    total_cost = fixed_cost + total_variable_cost

    # Calculate revenue
    participant_contributions = registration_fee * participants
    total_funding = participant_contributions + sponsorship
    shortfall = max(0, total_cost - total_funding)

    # Break-even calculation
    balance_per_participant = registration_fee - variable_cost

    print("\n===== EVENT FINANCIAL SUMMARY =====")
    print(f"Venue Cost: ₹{venue:.2f}")
    print(f"Equipment Cost: ₹{equipment:.2f}")
    print(f"Catering Cost: ₹{catering_per_person * participants:.2f}")
    print(f"Transport Cost: ₹{transport:.2f}")
    print(f"Certificate Cost: ₹{certificate_per_person * participants:.2f}")
    print(f"Total Event Cost: ₹{total_cost:.2f}")
    print(f"Participant Contributions: ₹{participant_contributions:.2f}")
    print(f"Sponsorship: ₹{sponsorship:.2f}")
    print(f"Total Funding: ₹{total_funding:.2f}")
    print(f"Sponsorship/Funding Shortfall: ₹{shortfall:.2f}")

    if balance_per_participant > 0:
        required = math.ceil(
            (fixed_cost - sponsorship) / balance_per_participant
        )
        required = max(0, required)

        print(f"Minimum Registrations to Break Even: {required}")

        if participants >= required:
            print("Status: Event budget breaks even.")
        else:
            print("Status: More registrations are needed.")
    else:
        print("Break-even is not possible through registration fees")
        print("at the current fee and variable cost.")


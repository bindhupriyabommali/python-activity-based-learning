
# Inventory Matrix Reconciliation

# List of products
products = ["Laptop", "Mouse", "Keyboard"]

# List of warehouses
warehouses = ["Warehouse A", "Warehouse B", "Warehouse C"]

# Inventory matrix: rows represent products, columns represent warehouses
inventory = [
    [50, 30, 20],   # Laptop quantities
    [100, 40, 60],  # Mouse quantities
    [25, 50, 15]    # Keyboard quantities
]

# Target stock required in each warehouse for each product
target = [
    [40, 35, 25],
    [80, 60, 60],
    [30, 30, 30]
]

print("===== INVENTORY MATRIX RECONCILIATION =====")

for i in range(len(products)):
    print("\nProduct:", products[i])

    surplus = []
    shortage = []

    # Compare current stock with target stock
    for j in range(len(warehouses)):
        difference = inventory[i][j] - target[i][j]

        if difference > 0:
            surplus.append([j, difference])
        elif difference < 0:
            shortage.append([j, abs(difference)])

    # Display shortages and surpluses
    if surplus:
        print("Surplus:")
        for item in surplus:
            print(warehouses[item[0]], ":", item[1], "units")

    if shortage:
        print("Shortage:")
        for item in shortage:
            print(warehouses[item[0]], ":", item[1], "units")

    # Calculate transfers between warehouses
    print("Required Transfers:")

    s = 0
    d = 0

    while s < len(surplus) and d < len(shortage):
        transfer = min(surplus[s][1], shortage[d][1])

        print(
            warehouses[surplus[s][0]], "->",
            warehouses[shortage[d][0]],
            ":", transfer, "units"
        )

        surplus[s][1] -= transfer
        shortage[d][1] -= transfer

        if surplus[s][1] == 0:
            s += 1

        if shortage[d][1] == 0:
            d += 1

    if not surplus and not shortage:
        print("No transfers required.")

print("\n===== RECONCILIATION COMPLETED =====")

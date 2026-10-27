
# Smart Canteen Order and Stock Management

# Menu with prices and available stock
menu = {
    "Idly": {"price": 30, "stock": 20},
    "Dosa": {"price": 50, "stock": 15},
    "Meals": {"price": 80, "stock": 10},
    "Tea": {"price": 10, "stock": 25},
    "Juice": {"price": 40, "stock": 12}
}

total_sales = 0
total_orders = 0

print("===== SMART CANTEEN MANAGEMENT =====")

while True:
    print("\n--- CANTEEN MENU ---")
    for item, details in menu.items():
        print(f"{item}: Rs.{details['price']} "
              f"(Available: {details['stock']})")

    print("\n1. Place Order")
    print("2. View Daily Sales")
    print("3. View Remaining Stock")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item name: ").title()

        if item not in menu:
            print("Invalid item! Please select from the menu.")
            continue

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if quantity > menu[item]["stock"]:
            print("Order rejected! Insufficient stock.")
            print("Available quantity:", menu[item]["stock"])
            continue

        # Calculate bill and update stock
        bill = menu[item]["price"] * quantity
        menu[item]["stock"] -= quantity
        total_sales += bill
        total_orders += 1

        print("\n----- BILL -----")
        print("Item:", item)
        print("Quantity:", quantity)
        print("Price per item: Rs.", menu[item]["price"])
        print("Total bill: Rs.", bill)
        print("Order placed successfully!")

    elif choice == "2":
        print("\n----- DAILY SALES SUMMARY -----")
        print("Total successful orders:", total_orders)
        print("Total sales: Rs.", total_sales)

    elif choice == "3":
        print("\n----- REMAINING STOCK -----")
        for item, details in menu.items():
            print(item, ":", details["stock"], "items")

    elif choice == "4":
        print("\n===== FINAL DAILY SUMMARY =====")
        print("Total successful orders:", total_orders)
        print("Total sales: Rs.", total_sales)
        print("\nRemaining Stock:")
        for item, details in menu.items():
            print(item, ":", details["stock"], "items")

        print("Thank you for using Smart Canteen!")
        break

    else:
        print("Invalid choice! Please try again.")

inventory = {}

while True:
    print("\n----- Inventory Management -----")
    print("1. Add Item")
    print("2. Update Quantity")
    print("3. Remove Item")
    print("4. Display Inventory")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        inventory[item] = qty

    elif choice == 2:
        item = input("Enter item name: ")
        if item in inventory:
            qty = int(input("Enter new quantity: "))
            inventory[item] = qty
        else:
            print("Item not found")

    elif choice == 3:
        item = input("Enter item name: ")
        if item in inventory:
            del inventory[item]
        else:
            print("Item not found")

    elif choice == 4:
        print("\nInventory:")
        for item, qty in inventory.items():
            print(item, ":", qty)

    elif choice == 5:
        break

    else:
        print("Invalid choice")

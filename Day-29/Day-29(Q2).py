arr = []

while True:
    print("\n----- Array Operations -----")
    print("1. Insert Element")
    print("2. Delete Element")
    print("3. Search Element")
    print("4. Display Array")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        num = int(input("Enter element: "))
        arr.append(num)

    elif choice == 2:
        num = int(input("Enter element to delete: "))
        if num in arr:
            arr.remove(num)
            print("Deleted successfully")
        else:
            print("Element not found")

    elif choice == 3:
        num = int(input("Enter element to search: "))
        if num in arr:
            print("Element found")
        else:
            print("Element not found")

    elif choice == 4:
        print("Array:", arr)

    elif choice == 5:
        break

    else:
        print("Invalid choice")

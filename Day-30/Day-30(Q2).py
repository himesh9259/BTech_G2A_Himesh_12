books = []

while True:
    print("\n----- Library System -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        books.append(book)

    elif choice == 2:
        book = input("Enter book to issue: ")
        if book in books:
            books.remove(book)
            print("Book issued")
        else:
            print("Book not available")

    elif choice == 3:
        book = input("Enter book to return: ")
        books.append(book)
        print("Book returned")

    elif choice == 4:
        print("Available Books:", books)

    elif choice == 5:
        break

    else:
        print("Invalid choice")

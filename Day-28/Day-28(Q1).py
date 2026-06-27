# Library Management System

library = {}

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        library[book_id] = {
            "Title": title,
            "Author": author
        }
        print("Book added successfully!")

    elif choice == '2':
        if library:
            print("\nAvailable Books:")
            for book_id, details in library.items():
                print(f"ID: {book_id}, Title: {details['Title']}, Author: {details['Author']}")
        else:
            print("No books available.")

    elif choice == '3':
        book_id = input("Enter Book ID to search: ")
        if book_id in library:
            print(library[book_id])
        else:
            print("Book not found.")

    elif choice == '4':
        book_id = input("Enter Book ID to remove: ")
        if book_id in library:
            del library[book_id]
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

# Student Record Management System

students = {}

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        students[roll] = {"Name": name, "Age": age}
        print("Student added successfully!")

    elif choice == '2':
        if students:
            for roll, details in students.items():
                print(f"Roll No: {roll}, Name: {details['Name']}, Age: {details['Age']}")
        else:
            print("No records found.")

    elif choice == '3':
        roll = input("Enter Roll Number to search: ")
        if roll in students:
            print(students[roll])
        else:
            print("Student not found.")

    elif choice == '4':
        roll = input("Enter Roll Number to delete: ")
        if roll in students:
            del students[roll]
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

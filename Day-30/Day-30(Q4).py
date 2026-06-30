students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        students[roll] = [name, marks]

    elif choice == 2:
        print("\nStudent Records:")
        for roll, data in students.items():
            print("Roll:", roll, "Name:", data[0], "Marks:", data[1])

    elif choice == 3:
        roll = input("Enter Roll No: ")
        if roll in students:
            print("Name:", students[roll][0])
            print("Marks:", students[roll][1])
        else:
            print("Student not found")

    elif choice == 4:
        roll = input("Enter Roll No: ")
        if roll in students:
            name = input("Enter New Name: ")
            marks = int(input("Enter New Marks: "))
            students[roll] = [name, marks]
            print("Record updated")
        else:
            print("Student not found")

    elif choice == 5:
        roll = input("Enter Roll No: ")
        if roll in students:
            del students[roll]
            print("Record deleted")
        else:
            print("Student not found")

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

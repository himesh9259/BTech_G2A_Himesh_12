names = []
marks = []

while True:
    print("\n----- Student Record System -----")
    print("1. Add Student")
    print("2. Display Records")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        mark = int(input("Enter marks: "))
        names.append(name)
        marks.append(mark)

    elif choice == 2:
        print("\nStudent Records")
        for i in range(len(names)):
            print(names[i], "-", marks[i])

    elif choice == 3:
        name = input("Enter student name: ")
        if name in names:
            index = names.index(name)
            print("Marks:", marks[index])
        else:
            print("Student not found")

    elif choice == 4:
        break

    else:
        print("Invalid choice")

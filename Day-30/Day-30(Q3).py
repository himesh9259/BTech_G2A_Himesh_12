employees = {}

while True:
    print("\n----- Employee Management -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        employees[emp_id] = name

    elif choice == 2:
        for emp_id, name in employees.items():
            print(emp_id, "-", name)

    elif choice == 3:
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print("Employee Name:", employees[emp_id])
        else:
            print("Employee not found")

    elif choice == 4:
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted")
        else:
            print("Employee not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")

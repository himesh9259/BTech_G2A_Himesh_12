# Employee Management System

employees = {}

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Remove Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")

        employees[emp_id] = {
            "Name": name,
            "Department": department
        }
        print("Employee added successfully!")

    elif choice == '2':
        if employees:
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}, Name: {details['Name']}, Department: {details['Department']}")
        else:
            print("No employee records found.")

    elif choice == '3':
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print(employees[emp_id])
        else:
            print("Employee not found.")

    elif choice == '4':
        emp_id = input("Enter Employee ID to remove: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee removed successfully!")
        else:
            print("Employee not found.")

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

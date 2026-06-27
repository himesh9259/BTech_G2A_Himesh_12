# Salary Management System

while True:
    print("\n--- Salary Management System ---")

    emp_name = input("Enter Employee Name: ")
    basic = float(input("Enter Basic Salary: "))

    hra = 0.20 * basic
    da = 0.10 * basic
    pf = 0.08 * basic

    gross_salary = basic + hra + da
    net_salary = gross_salary - pf

    print("\n----- Salary Slip -----")
    print("Employee Name :", emp_name)
    print("Basic Salary  :", basic)
    print("HRA (20%)     :", hra)
    print("DA (10%)      :", da)
    print("PF (8%)       :", pf)
    print("Gross Salary  :", gross_salary)
    print("Net Salary    :", net_salary)

    ch = input("\nDo you want to continue? (y/n): ")
    if ch.lower() != 'y':
        break

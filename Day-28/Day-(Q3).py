# Ticket Booking System

available_tickets = 50

while True:
    print("\n--- Ticket Booking System ---")
    print("1. Book Ticket")
    print("2. Check Available Tickets")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        tickets = int(input("Enter number of tickets to book: "))

        if tickets <= available_tickets:
            available_tickets -= tickets
            print(f"{tickets} ticket(s) booked successfully.")
        else:
            print("Not enough tickets available.")

    elif choice == '2':
        print("Available Tickets:", available_tickets)

    elif choice == '3':
        print("Booking system closed.")
        break

    else:
        print("Invalid choice!")

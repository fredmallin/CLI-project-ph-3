from models import (
    add_customer, get_all_customers,
    add_car, get_cars_by_customer,
    book_appointment, get_service_history
)
def main_menu():
    while True:
        print("\n=== Car Service Booking CLI ===")
        print("1. Add Customer")
        print("2. Add Car")
        print("3. Book Appointment")
        print("4. View Customer Cars")
        print("5. View Car Service History")
        print("6. Exit")

        choice = input("Choose an option: ")

  if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_customer(name, phone, email)
            print(" Customer added successfully!")

 elif choice == "2":
            customers = get_all_customers()
            print("\nAvailable Customers:")
            for c in customers:
                print(f"{c[0]} - {c[1]} ({c[2]})")
            customer_id = input("Enter customer ID for this car: ")
            model = input("Enter car model: ")
            year = input("Enter car year: ")
            add_car(customer_id, model, year)
            print(" Car registered successfully!")


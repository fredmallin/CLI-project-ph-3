from models import (
    add_customer, get_all_customers,
    add_car, get_cars_by_customer,
    book_appointment, get_service_history,
    delete_appointment
)

def main_menu():
    while True:
        print("\n=== Car Service Booking CLI ===")
        print("1. Add Customer")
        print("2. Add Car")
        print("3. Book Appointment")
        print("4. View Customer Cars")
        print("5. View Car Service History")
        print("6. Delete Appointment")
        print("7. Exit")

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

        elif choice == "3":
            customer_id = input("Enter customer ID: ")
            cars = get_cars_by_customer(customer_id)
            if not cars:
                print(" No cars found for this customer.")
                continue
            print("\nCars:")
            for car in cars:
                print(f"{car[0]} - {car[2]} ({car[3]})")
            car_id = input("Enter car ID for service: ")
            service_type = input("Enter service type (e.g., Oil Change, Tire Rotation): ")
            date = input("Enter service date (YYYY-MM-DD): ")
            book_appointment(car_id, service_type, date)
            print("✅Appointment booked successfully!")

        elif choice == "4":
            customer_id = input("Enter customer ID: ")
            cars = get_cars_by_customer(customer_id)
            if not cars:
                print(" No cars found for this customer.")
            else:
                print("\nCars for this customer:")
                for car in cars:
                    print(f"{car[0]} - {car[2]} ({car[3]})")

        elif choice == "5":
            car_id = input("Enter car ID: ")
            history = get_service_history(car_id)
            if not history:
                print(" No service history found for this car.")
            else:
                print("\nService History:")
                for appt in history:
                    print(f"ID: {appt[0]} | Service: {appt[2]} | Date: {appt[3]} | Status: {appt[4]}")

        elif choice == "6":
            car_id = input("Enter car ID to view appointments: ")
            history = get_service_history(car_id)
            if not history:
                print("No service history found for this car.")
            else:
                print("\nAppointments for this car:")
                for appt in history:
                    print(f"ID: {appt[0]} | Service: {appt[2]} | Date: {appt[3]} | Status: {appt[4]}")
                appt_id = input("Enter Appointment ID to delete: ")
                delete_appointment(appt_id)
                print(" Appointment deleted successfully!")

        elif choice == "7":
            print(" Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

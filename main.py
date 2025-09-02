from lib.cli import *
from lib.database import Base, engine


Base.metadata.create_all(engine)

def main():
    while True:
        print("\n=== Car Service CLI ===")
        print("1. Add Customer")
        print("2. Add Car")
        print("3. Book Service Appointment")
        print("4. View Customer Cars")
        print("5. View Service History")
        print("6. Delete Customer/Car/Service")
        print("7. Exit")

        choice = input("Choose an option: ").strip()
        menu = {
            "1": add_customer,
            "2": add_car,
            "3": add_service,
            "4": list_cars,
            "5": view_service_history,
            "6": delete_entry,
        }

        if choice == "7":
            print("Goodbye!")
            break

        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

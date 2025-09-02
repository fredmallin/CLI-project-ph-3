from datetime import datetime
from sqlalchemy.orm import Session
from prettytable import PrettyTable
from lib.database import SessionLocal
from lib.models import Customer, Car, Service


db: Session = SessionLocal()


def add_customer():
    name = input("Customer Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    customer = Customer(name=name, phone=phone, email=email)
    db.add(customer)
    db.commit()
    print("Customer added successfully!")

def list_customers():
    customers = db.query(Customer).all()
    table = PrettyTable(["ID", "Name", "Phone", "Email"])
    for c in customers:
        table.add_row([c.id, c.name, c.phone, c.email])
    print(table)

def add_car():
    list_customers()
    customer_id = int(input("Customer ID to link car: ").strip())
    customer = db.query(Customer).get(customer_id)
    if not customer:
        print("Customer not found.")
        return
    model = input("Car Model: ").strip()
    year = input("Car Year: ").strip()
    car = Car(model=model, year=year, owner=customer)
    db.add(car)
    db.commit()
    print("Car added successfully!")

def list_cars():
    cars = db.query(Car).all()
    table = PrettyTable(["ID", "Model", "Year", "Owner"])
    for c in cars:
        table.add_row([c.id, c.model, c.year, c.owner.name])
    print(table)

def add_service():
    list_cars()
    car_id = int(input("Car ID for service: ").strip())
    car = db.query(Car).get(car_id)
    if not car:
        print("Car not found.")
        return
    service_type = input("Service Type: ").strip()
    date_str = input("Service Date (YYYY-MM-DD): ").strip()
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    service = Service(service_type=service_type, date=date, car=car)
    db.add(service)
    db.commit()
    print("Service added successfully!")

def view_service_history():
    list_cars()
    car_id = int(input("Car ID to view history: ").strip())
    car = db.query(Car).get(car_id)
    if not car:
        print("Car not found.")
        return
    table = PrettyTable(["ID", "Service Type", "Date", "Status"])
    for s in car.services:
        table.add_row([s.id, s.service_type, s.date, s.status])
    print(table)

def delete_entry():
    print("1. Delete Customer\n2. Delete Car\n3. Delete Service")
    choice = input("Choose type to delete: ").strip()
    if choice == "1":
        list_customers()
        cid = int(input("Customer ID to delete: ").strip())
        customer = db.query(Customer).get(cid)
        if customer:
            db.delete(customer)
            db.commit()
            print("Customer deleted!")
    elif choice == "2":
        list_cars()
        cid = int(input("Car ID to delete: ").strip())
        car = db.query(Car).get(cid)
        if car:
            db.delete(car)
            db.commit()
            print("Car deleted!")
    elif choice == "3":
        view_service_history()
        sid = int(input("Service ID to delete: ").strip())
        service = db.query(Service).get(sid)
        if service:
            db.delete(service)
            db.commit()
            print("Service deleted!")
    else:
        print("Invalid choice")

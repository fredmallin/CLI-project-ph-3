# CLI-project-ph-3

# project name

Car Service Booking CLI


# Video Demo
https://www.loom.com/share/a05c331bf4e5408cb806a2e5d94b3adb?sid=5fd2d775-d856-40a4-8292-02376d60449d  (first 5min)

 https://www.loom.com/share/e64ea9dd649b4937884b5d78c88ae9e8?sid=40b6255b-7636-4c85-a49e-bee1e0e9f7d1  (second 3 min)

# Author
Fredrick mwangi

# Problem Statement
Car garages and service stations often keep records on paper or in memory. This makes it hard to track customers, their cars and service appointments. As a result, services can be forgotten, appointments missed, and customers may not know their car’s service history.

# Solution Statement
The Car Service Booking CLI is a simple text-based program that helps garages and car owners keep records in one place. It allows adding customers, registering their cars, and booking service appointments. It also keeps a clear history of services so nothing is lost or forgotten.

# Project features
1.Add Customers- Save customer details like name, phone number, and email.
2.Register Cars -add car details ( model, year) and link them to the right customer.
3.Book Service Appointments - Schedule car services by date and type 
4.View Customer Cars - See all cars that belong to a specific customer.
5.See a car’s full service history- lists all past appointments with dates and status.
6.Delete feature - deletes appointments
7.simple CLI menu - (Add Customer, Add Car, Book Appointment, View Cars, View Service History, Exit)

# CLI Functions Workflow
# Main Menu (main())

Displays the available options (View Customers, Add Customer, Add Car, Book Service, View Service History, Exit).
Routes user choice to the correct function.

# View Customers (view_customers())
Fetches all customers from the database.
Prints their names, contact numbers, and cars.

# Add Customer (add_customer())
Prompts for customer name and contact number.
Saves a new Customer record to the database.

# Add Car (add_car())
Prompts for customer ID, car model, year, and license plate.
Links the car to the correct customer and saves to the database.

# Book Service (book_service())
Prompts for car ID, service type (oil change, tire replacement, etc.), and date.
Creates a new Service entry tied to the selected car.

# View Service History (view_service_history())
Prompts for customer ID or car ID.
Displays all past services (type, date, status) in order.

# Exit (exit_cli())
Ends the program with a goodbye message.
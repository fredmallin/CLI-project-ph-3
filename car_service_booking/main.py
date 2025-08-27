from database import setup_database
from menu import main_menu

if __name__ == "__main__":
    setup_database()
    main_menu()
def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Customers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)
# Cars Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            model TEXT NOT NULL,
            year INTEGER,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    """)
 # Appointments Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER,
            service_type TEXT NOT NULL,
            date TEXT NOT NULL,
            status TEXT DEFAULT 'Scheduled',
            FOREIGN KEY(car_id) REFERENCES cars(id)
        )
    """)

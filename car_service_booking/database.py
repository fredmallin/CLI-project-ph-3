import sqlite3

def get_connection():
    return sqlite3.connect("car_service.db")

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Customers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)

    # Cars
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            model TEXT NOT NULL,
            year INTEGER,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
    """)

    # Appointments
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

    conn.commit()
    conn.close()

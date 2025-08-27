import sqlite3

def get_connection():
    return sqlite3.connect("car_service.db")

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

from database import get_connection

# ---------- Customers ----------
def add_customer(name, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    conn.close()
def get_all_customers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    conn.close()
    return rows
# ---------- Cars ----------
def add_car(customer_id, model, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cars (customer_id, model, year) VALUES (?, ?, ?)", (customer_id, model, year))
    conn.commit()
    conn.close()

def get_cars_by_customer(customer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cars WHERE customer_id = ?", (customer_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# ---------- Appointments ----------
def book_appointment(car_id, service_type, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (car_id, service_type, date) VALUES (?, ?, ?)", (car_id, service_type, date))
    conn.commit()
    conn.close()

def get_service_history(car_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE car_id = ?", (car_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_appointment(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
    conn.commit()
    conn.close()

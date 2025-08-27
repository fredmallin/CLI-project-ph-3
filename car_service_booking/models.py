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


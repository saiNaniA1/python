import pymysql
from tkinter import messagebox

# Establish a connection to MySQL
try:
    conn = pymysql.connect(host='localhost', user='root', password='2001', database='employee_data')
    mycursor = conn.cursor()
    print("Connection to the database was successful!")

    # Create table if it doesn't exist
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS DATA (
            id VARCHAR(30) PRIMARY KEY,
            Name VARCHAR(50),
            Phone VARCHAR(15),
            Role VARCHAR(20),
            Gender VARCHAR(20),
            Salary DECIMAL(10,2)
        )
    """)
    print("Table setup completed.")
except pymysql.MySQLError as e:
    print(f"Database Connection Error: {e}")

# Function to insert a new employee
def insert(id, name, phone, role, gender, salary):
    try:
        query = "INSERT INTO DATA (id, Name, Phone, Role, Gender, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
        mycursor.execute(query, (id, name, phone, role, gender, salary))
        conn.commit()
        print("Employee record inserted successfully.")
    except pymysql.MySQLError as e:
        print(f"Insert Error: {e}")

# Function to check if an ID exists
def id_exists(id):
    try:
        mycursor.execute("SELECT id FROM DATA WHERE id = %s", (id,))
        result = mycursor.fetchone()
        return result is not None
    except pymysql.MySQLError as e:
        print(f"ID Check Error: {e}")
        return False

# Function to fetch all employees
def fetch_employee():
    try:
        mycursor.execute("SELECT * FROM DATA")
        result = mycursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        print(f"Fetch Error: {e}")
        return []

# Function to search for employees
def search_employee(field, value):
    try:
        # Build a dynamic query to search based on the provided field and value
        query = f"SELECT * FROM DATA WHERE {field} LIKE %s"
        mycursor.execute(query, (f"%{value}%",))
        result = mycursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        print(f"Search Error: {e}")
        return []

# Function to delete an employee by ID
def delete(employee_id):
    try:
        query = "DELETE FROM DATA WHERE id = %s"
        mycursor.execute(query, (employee_id,))
        conn.commit()
        print(f"Employee with ID {employee_id} deleted successfully.")
    except pymysql.MySQLError as e:
        print(f"Delete Error: {e}")
        return False
    return True

# Function to delete all employees
def delete_all():
    try:
        query = "DELETE FROM DATA"
        mycursor.execute(query)
        conn.commit()
        print("All employees deleted successfully.")
    except pymysql.MySQLError as e:
        print(f"Delete All Error: {e}")
        return False
    return True


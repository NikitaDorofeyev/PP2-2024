import psycopg2
from config import host, database, user, password
import csv

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
connection.autocommit = True
cursor = connection.cursor()

# Check server version
cursor.execute("SELECT version();")
print(f"Server version: {cursor.fetchone()}")

# Create users table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        first_name varchar(50),
        phone_number varchar(20)
    );
""")
print("Table created!")

# Insert data from CSV
def insert_from_csv():
    with open('Lab10/contacts.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO users VALUES (%s,%s)", row)

# Insert data manually
def insert_manually():
    entries = []
    while True:
        print("Enter name (or 'done' to finish): ")
        name = input()
        if name.lower() == 'done':
            break
        print("Enter phone number: ")
        phone = input()
        entries.append((name, phone))

    if entries:
        cursor.executemany("INSERT INTO users VALUES (%s, %s)", entries)
        print("Entries inserted successfully.")


def update_user():
    print("Enter name of user to update: ")
    name = input()

    # Check if the user exists
    cursor.execute("SELECT * FROM users WHERE first_name = %s", (name,))
    user_data = cursor.fetchone()

    if user_data:
        print("Enter new phone number: ")
        phone = input()

        # Update the phone number
        cursor.execute("UPDATE users SET phone_number = %s WHERE first_name = %s", (phone, name))
        print("User information updated successfully.")
    else:
        print("User not found.")


# Display table data
def show_table():
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    for row in result:
        print(row)

def delete_user():
    identifier = input("Enter username or phone number of user to delete: ")

    cursor.execute("DELETE FROM users WHERE first_name = %s OR phone_number = %s", (identifier, identifier))

    # Check if any row was affected by the deletion
    if cursor.rowcount > 0:
        print("User deleted successfully.")
    else:
        print("User not found.")


# Main menu
while True:
    print("\nMain Menu:")
    print("1. Insert from CSV")
    print("2. Insert manually")
    print("3. Update user")
    print("4. Show table")
    print("5. Delete user")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        insert_from_csv()
    elif choice == '2':
        insert_manually()
    elif choice == '3':
        update_user()
    elif choice == '4':
        show_table()
    elif choice == '5':
        delete_user()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

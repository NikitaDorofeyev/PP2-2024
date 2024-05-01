import psycopg2
from config import host, database, user, password
import csv

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
connection.autocommit = True
cursor = connection.cursor()

cursor.execute(
    "SELECT version();"
)
print(f"Server version: {cursor.fetchone()}")

# create table
# with connection.cursor() as cursor:

# Design tables for PhoneBook.

cursor.execute(
    """CREATE TABLE IF NOT EXISTS users(
        first_name varchar(50),
        phone_number varchar(20));"""
)
# connection.commit()
print(f"Table created!")

# Implement two ways of inserting data into the PhoneBook

out = "yes"
while True:
    print("Insert (csv) file? yes or no")
    out = input()
    if out == "no":
        break
    with open('Lab10/contacts.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO users VALUES (%s,%s)", row)
    break
while True:
    print("Insert your phone and name? yes or no")
    out = input()
    if out == "no":
        break
    print("write your name: ")
    name = input()
    print("write your number: ")
    phone = input()
    cursor.execute(f"""INSERT INTO users (first_name, phone_number) VAlUES
('{name}', '{phone}');""")
    break

# Implement updating data in the table (change user first name or phone)

while True:
    print("Change some data? yes or no")
    out = input()
    if out == "no":
        break
    print("Change name or number: name or number")
    out = input()
    if out == "name":
        print("Write phone number to change name: ")
        phone = input()
        print("Write name of user:")
        name = input()
        cursor.execute(f"""UPDATE users
            SET first_name = '{name}'
            WHERE phone_number = '{phone}';""")
    else:
        print("Write name to change number: ")
        phone = input()
        print("Write phone number:")
        name = input()
        cursor.execute(f"""UPDATE users
            SET phone_number = '{name}'
            WHERE first_name = '{phone}';""")
    break

# Querying data from the tables (with different filters)
while True:
    print("Show table? yes or no")
    out = input()
    if out == "no":
        break
    print("Phones or names or all? phone or name or all")
    out = input()
    if out == "name":
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row[0])
    if out == "phone":
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row[1])
    if out == "all":
        cursor.execute("""SELECT * FROM users""")
        result = cursor.fetchall()
        for row in result:
            print(row[0], "phone -", row[1])
    break

# DELETE DATA

while True:
    print("Delete more users? yes or no")
    if input() == "no":
        break
    cursor.execute("""SELECT * FROM users""")
    result = cursor.fetchall()
    for row in result:
        print(row[0])
    print("wWite user name?")
    name = input()
    cursor.execute(f"""DELETE FROM users WHERE first_name='{name}';""")



 
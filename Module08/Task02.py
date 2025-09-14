import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="271197",
    database="airport",
    autocommit=True
)

cursor = connection.cursor()

area_code = input("Please enter area code: ")

sql = f"SELECT type, count(*) FROM airport WHERE iso_country = '{area_code}' group by type order by type"

cursor.execute(sql)

result = cursor.fetchall()

if result:
    print(f"Area code for the respective country is {area_code}.")
    for row in result:
        type, count = row
        print(f"{type}: {count}")
else:
    print(f"No airport found for the area code {area_code}.")
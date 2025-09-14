import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="271197",
    database="airport",
    autocommit=True
)

cursor = connection.cursor()

icao = input("Enter ICAO code: ")

sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao}'"
cursor.execute(sql)

result = cursor.fetchall()

if result:

    for row in result:

        print(f"Airport name: {row[0]}")
        print(f"Location (town): {row[1]}")
else:
    print("No airport found with that ICAO code.")



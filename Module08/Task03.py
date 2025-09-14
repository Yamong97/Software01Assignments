from geopy import distance
import mysql.connector

def icaoCoordinates(icao):
    sql = f"select latitude_deg, longitude_deg from airport where ident= '{icao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result) > 0:
        return result[0]
    else:
        return None

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="271197",
    database="airport",
    autocommit=True
)

user_coordinates01 = input("Enter first airport ICAO: ")
user_coordinates02 = input("Enter second airport ICAO: ")

coordinates01 = icaoCoordinates(user_coordinates01)
coordinates02 = icaoCoordinates(user_coordinates02)

if coordinates01 and coordinates02:
    distance_between_airports = distance.distance(coordinates01, coordinates02).km
    print(f"Distance between airports: {distance_between_airports:.2f} km")
else:
    print("One or both ICAO codes not found.")
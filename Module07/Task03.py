airports = {}

user = input("Please enter new, fetch or quit: ")

while user != "quit":
    if user == "new":
        ICAO = input("Please enter ICAO code: ")
        airport_name = input("Please enter airport name: ")
        airports[ICAO] = airport_name

    elif user == "fetch":
        ICAO = input("Please enter ICAO code: ")
        if ICAO in airports:
            print(airports[ICAO])
        else:
            print("Airport not found!")
    else:
        print("Please enter new or fetch: ")

    user = input("Please enter new, fetch or quit: ")

print("The program end!")





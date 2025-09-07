cities = []

for i in range (5):

    city = input("Please enter city name: ")

    cities.append(city)

print(f"The name of five cities are the following: ")
for city in cities:
    print(f"- {city}")



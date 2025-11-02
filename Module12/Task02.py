import requests

def weather():
    township = input("Enter the name of township/municipality: ")
    api_key = input("Enter your API key: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={township}&appid={api_key}"

    response = requests.get(url)


    if response.status_code == 200:
        data = response.json()

        description = data["weather"][0]["description"]

        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15

        print(f"Weather in {township} is: {description}")
        print(f"Temperature in {township} is: {temperature_celsius:.2f}°C")

weather()

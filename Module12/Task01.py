import requests


def chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke = data["value"]
        print(f"This is a Chuck Norris joke: {joke}")

chuck_norris_joke()

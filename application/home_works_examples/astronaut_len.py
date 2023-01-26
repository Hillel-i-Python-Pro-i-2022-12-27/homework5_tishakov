import requests
import json


def austronaut_len():
    response = requests.get("http://api.open-notify.org/astros.json")
    with open("info", "w") as file:
        file.write(response.text)
    answer = json.loads(response.text)
    for i in answer["people"]:
        print(i["name"])


print(austronaut_len())

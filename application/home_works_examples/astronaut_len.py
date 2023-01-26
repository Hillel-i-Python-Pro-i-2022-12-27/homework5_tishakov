import requests


def austronaut_len():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    answer = []
    while True:
        for i in data["people"]:
            answer.append(i["name"])
        return answer


print(austronaut_len())

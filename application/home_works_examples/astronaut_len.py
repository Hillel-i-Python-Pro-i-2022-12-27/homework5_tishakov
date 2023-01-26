import requests


# def get_info():
#     response = requests.get("http://api.open-notify.org/astros.json")
#     with open("info", "w") as file:
#         file.write(response.text)
#     answer = json.loads(response.text)
#     for i in answer["people"]:
#         print(i["name"])


def austronaut_len():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    answer = []
    while True:
        for i in data["people"]:
            answer.append(i["name"])
        return answer


print(austronaut_len())

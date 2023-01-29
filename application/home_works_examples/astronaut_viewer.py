import requests


def astronaut_viewer():
    data = requests.get("http://api.open-notify.org/astros.json")
    response = data.json()
    result = []
    for i in response["people"]:
        result.append(i["name"])
    return result


astronaut_viewer()

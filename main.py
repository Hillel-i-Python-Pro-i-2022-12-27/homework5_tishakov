# from reader import Reader
# import csv

from application.home_works_examples.read_text import read_text
from application.home_works_examples.generator_email import generator_email
from application.home_works_examples.astronaut_len import austronaut_len


# def get_info():
#     response = requests.get("http://api.open-notify.org/astros.json")
#     with open("info", "w") as file:
#         file.write(response.text)
#     answer = json.loads(response.text)
#     for i in answer["people"]:
#         print(i["name"])
#
#
# def csv_reader():
#     text = FILES_INPUT_FILES_CSV
#     # with Reader.readFromFile(open(text, newline="")) as file:
#     #     for line in file:
#     #         print(line)
#     with open(text,mode="r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             print(row)


def main():
    print("\tзадание 1 - чтенние файла по пути:\n", read_text())
    print("\tзадание 2 - сгенерировать 100 мэйлов:\n", len(generator_email()), generator_email())
    print("\tзадание 3 - вывести космонавтов:\n", austronaut_len())
    # print(csv_reader())


if __name__ == "__main__":
    main()

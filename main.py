# from reader import Reader
# import csv
# from application.config.paths import FILES_INPUT_FILES_CSV
from application.home_works_examples.read_text import read_text
from application.home_works_examples.generator_email import generator_email
from application.home_works_examples.astronaut_len import austronaut_len


#
# import csv
# with open(FILES_INPUT_FILES_CSV, newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(type(row))


def main():
    print("\tзадание 1 - чтенние файла по пути:\n", read_text())
    print("\tзадание 2 - сгенерировать 100 мэйлов:\n", generator_email())
    print("\tзадание 3 - вывести космонавтов:\n", austronaut_len())
    # print(csv_reader())


if __name__ == "__main__":
    main()

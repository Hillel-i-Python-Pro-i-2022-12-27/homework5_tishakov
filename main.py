import csv
import math

from application.config.paths import FILES_INPUT_CSV
from application.home_works_examples.read_text import read_text
from application.home_works_examples.generator_email import generator_email
from application.home_works_examples.astronaut_viewer import astronaut_viewer


def csv_reader():
    data = csv.DictReader(open(FILES_INPUT_CSV))
    data_height = []
    data_weight = []
    for row in data:
        data_height.append(row["Height(Inches)"])
        data_weight.append(row["Weight(Pounds)"])
        list_data_height = list(map(float, data_height))
        avg = math.fsum(list_data_height) / len(list_data_height)
    print(avg)


def main():
    print("\tзадание 1 - чтенние файла по пути:\n", read_text())
    print("\tзадание 2 - сгенерировать 100 мэйлов:\n", generator_email())
    print("\tзадание 3 - вывести космонавтов:\n", astronaut_viewer())
    print("\tзадание 4 - считать и если получиться посчитать:\n", csv_reader())


if __name__ == "__main__":
    main()

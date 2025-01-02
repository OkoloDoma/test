import csv
import json  # TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    dict_array = []
    with open(INPUT_FILENAME, 'r') as f:
        data = csv.DictReader(f)  # TODO считать содержимое csv файла
        for r in data:
            dict_array.append(r)

    with open(OUTPUT_FILENAME, 'w') as f:
        json.dump(dict_array, f, indent=4)
    return  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

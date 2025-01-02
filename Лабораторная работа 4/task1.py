# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:
        data = json.load(f)

    return round(sum([a["score"] * a["weight"] for a in data]), 3)

print(task())

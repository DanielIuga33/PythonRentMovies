from typing import List

from models.Client import Client


def show_all(entities):
    if len(entities) == 0:
        print("  There's no data to show !")
        return
    for entity in entities:
        print(entity)

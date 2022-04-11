import csv
import json
from csv import DictReader

""" Работа с тестовыми данными """

with open('../files/books.csv', newline='') as csv_file:
    books = DictReader(csv_file)
    size = books.__sizeof__() - 1
    with open("../files/users.json", "r") as json_file:
        users = json.loads(json_file.read())
        while size > 0:
            for user in users:
                if size == 0:
                    break
                if "books" not in user:
                    user["books"] = []
                # получаем следующую книгу
                book = next(books)
                # выдаем книгу
                user["books"].append(book)
                size -= 1
# сохраняем результат в файл в формате json
with open("../files/result.json", "w") as result_file:
    json.dump(users, result_file, indent=4)

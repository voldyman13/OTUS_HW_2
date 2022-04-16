import csv
import json
from csv import DictReader

""" Работа с тестовыми данными """

# Получаем список книг из файла books.csv
with open('../files/books.csv', newline='') as csv_file:
    books = list(DictReader(csv_file))

# Получаем список пользователей из файла users.json
with open("../files/users.json", "r") as json_file:
    users = json.loads(json_file.read())

index = 0
for book in books:
    if index == len(users):
        index = 0
    if "books" not in users[index]:
        user = {
            "name": users[index]["name"],
            "gender": users[index]["gender"],
            "address": users[index]["address"],
            "age": users[index]["age"],
            "books": []
        }
        # перезаписываем данные пользователя оставляя только необходимые данные и добавляем новый аргумент books[]
        users[index].clear()
        users[index] = user
    # выдаем книгу
    users[index]["books"].append(
        {"Title": book["Title"], "Author": book["Author"], "Genre": book["Genre"], "Pages": book["Pages"]})
    index += 1
# сохраняем результат в файл в формате json
with open("../files/result.json", "w") as result_file:
    json.dump(users, result_file, indent=4)

from dotenv import load_dotenv
import os
import csv
import json
from math import floor, ceil


def add_info(src, fields, *additional_fields):
    result = {field: src[field] for field in fields}
    for field in additional_fields:
        result.update(field)
    return result


load_dotenv()

PATH_TO_FILES = os.getenv("PATH_TO_FILES")

books = []
users = None
result = []
result_user_fields = ("name", "gender", "address", "age")
result_book_fields = ("title", "author", "pages", "genre")
csv_map = None

with open(f"{PATH_TO_FILES}/books.csv", newline="") as books_file:
    books_reader = csv.reader(books_file)
    next(books_reader)

    for row in books_reader:
        books.append(dict(zip(result_book_fields, row)))
    # books = [book for book in csv.reader(f, delimiter=",")]
    # csv_map = {books[0].index(header): header.casefold() for header in books[0]}
    # books.pop(0)
    # books = list(map(lambda b: {csv_map[b.index(field)]: field for field in b}, books))

with open(f"{PATH_TO_FILES}/users.json", newline="") as f:
    users = json.load(f)

books_amnt = len(books)
users_amnt = len(users)
clng = ceil(books_amnt / users_amnt)
flr = floor(books_amnt / users_amnt)
remaining_books_amnt = books_amnt - (flr * users_amnt)
start_ix = 0
stop_ix = start_ix

for user in users:
    stop_ix += clng if remaining_books_amnt > 0 else flr
    remaining_books_amnt -= 1
    result.append(
        add_info(
            user,
            result_user_fields,
            {
                "books": [
                    add_info(books[ix], result_book_fields)
                    for ix in range(start_ix, stop_ix)
                ]
            },
        )
    )
    start_ix = stop_ix

with open("result.json", "w") as f:
    json.dump(result, f, indent=4)

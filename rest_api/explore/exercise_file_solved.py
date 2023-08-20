# REST API Exercise - Solved

# Note: Before running this file, make sure the REST API server is running.
# You can start it by running `python server.py` in a separate terminal window.

import requests

# Task 1: GET Request
get_books_response = requests.get("http://localhost:8000/books").json()
print("Task 1: GET all books:", get_books_response)

# Task 2: GET Request with URL Arguments
get_book_by_id_response = requests.get("http://localhost:8000/books/1").json()
print("Task 2: GET book by ID:", get_book_by_id_response)

# Task 3: POST Request
post_book_response = requests.post(
    "http://localhost:8000/books", json={"title": "New Book", "author": "New Author"}
).json()
print("Task 3: POST a new book:", post_book_response)

# Task 4: PUT Request
put_book_response = requests.put(
    "http://localhost:8000/books/1",
    json={"title": "Updated Book", "author": "Updated Author"},
).json()
print("Task 4: PUT to update a book:", put_book_response)

# Task 5: DELETE Request
delete_book_response = requests.delete("http://localhost:8000/books/1").json()
print("Task 5: DELETE a book:", delete_book_response)


# REST API Exercise

This exercise is designed to help you get familiar with making HTTP requests to a REST API using Python.

## Pre-exercise: Explore the API
1. Start the REST API server by running `python server.py` in a separate terminal window.
2. Open your web browser and navigate to [http://localhost:5000/api/](http://localhost:5000/api/) to explore the API documentation.
3. (Optional) Use Insomnia or Postman to make requests to the following endpoints and observe the responses:
    - GET http://localhost:5000/books
    - GET http://localhost:5000/books/1
    - POST http://localhost:5000/books (Body: `{"title": "New Book", "author": "New Author"}`)
    - PUT http://localhost:5000/books/1 (Body: `{"title": "Updated Book", "author": "Updated Author"}`)
    - DELETE http://localhost:5000/books/1

## Instructions
# Once you are familiar with the API, proceed to complete the following tasks by filling in the code.

### Task 1: GET Request
# Perform a GET request to fetch all available books from the server.
get_books_response = None  # Your code here

### Task 2: GET Request with URL Arguments
# Fetch details of a specific book by its ID (e.g., ID = 1)
get_book_by_id_response = None  # Your code here

### Task 3: POST Request
# Add a new book to the server's book list.
post_book_response = None  # Your code here

### Task 4: PUT Request
# Update the details of a book by its ID (e.g., ID = 1)
put_book_response = None  # Your code here

### Task 5: DELETE Request
# Delete a book by its ID (e.g., ID = 1)
delete_book_response = None  # Your code here


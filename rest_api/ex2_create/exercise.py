
# REST API Server Exercise with Flask

# In this exercise, you will create a simple REST API server using Flask. The server will manage a list of books, supporting operations to list all books, get details of a specific book, add a new book, update an existing book, and delete a book.

## Learning Objectives
# 1. Understand RESTful API design.
# 2. Learn to implement CRUD operations using Flask.
# 3. Familiarize yourself with HTTP methods (GET, POST, PUT, DELETE).

## Pre-requisites
# - Python 3.x
# - Flask

# If you haven't installed Flask, you can install it using pip:
# ```
# pip install Flask
# ```

## Tasks

### Task 1: Initialize Flask App
# Create a Flask app and define a route for the root URL ("/") that returns a welcome message.

### Task 2: Create Book list
# Define a Python list to serve as an in-memory database for books. 

### Task 3: List All Books (GET /books)
# Create a route to list all books. The endpoint should be `/books` and the method should be GET.

### Task 4: Get a Specific Book (GET /books/<id>)
# Create a route to get details of a specific book by its ID. The endpoint should be `/books/<id>` and the method should be GET.

### Task 5: Add a New Book (POST /books)
# Create a route to add a new book. The endpoint should be `/books` and the method should be POST.

### Task 6: Update a Book (PUT /books/<id>)
# Create a route to update an existing book by its ID. The endpoint should be `/books/<id>` and the method should be PUT.

### Task 7: Delete a Book (DELETE /books/<id>)
# Create a route to delete a book by its ID. The endpoint should be `/books/<id>` and the method should be DELETE.

## Tips
# - Use `@app.route` to define routes.
# - Use `request.json` to get JSON data from the request.
# - Use `jsonify` to convert Python dictionaries to JSON.

## Bonus
# Create an API documentation using Swagger.

# Good luck and have fun coding!

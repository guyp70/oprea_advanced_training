
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database of books
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
]

@app.route("/")
def hello():
    return "Welcome to the Book API!"

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

@app.route("/books", methods=["POST"])
def post_book():
    new_book = request.json
    new_book["id"] = max([book["id"] for book in books]) + 1
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def put_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    book.update(request.json)
    return jsonify(book)

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": f"Book with ID {book_id} has been deleted"})

if __name__ == "__main__":
    app.run(debug=True)

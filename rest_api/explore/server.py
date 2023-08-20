from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Book(BaseModel):
    id: int = None
    title: str
    author: str


# In-memory database of books
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
]


@app.get("/books", response_model=List[Book])
async def get_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books", response_model=Book)
async def post_book(new_book: Book):
    new_book.id = max([book["id"] for book in books]) + 1 if books else 1
    books.append(new_book.dict())
    return new_book


@app.put("/books/{book_id}", response_model=Book)
async def put_book(book_id: int, updated_book: Book):
    book = next((item for item in books if item["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    book.update(updated_book.dict())
    return updated_book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    global books
    books = [book for book in books if book["id"] != book_id]
    return {"message": f"Book with ID {book_id} has been deleted"}

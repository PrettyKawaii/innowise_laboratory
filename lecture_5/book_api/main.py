from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Book, get_db

app = FastAPI()


@app.post("/books/")
def add_book(book: dict, db: Session = Depends(get_db)):
    """Add a new book to the database."""
    new_book = Book(
        title=book["title"],
        author=book["author"],
        year=book.get("year")  # Optional field
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {
        "id": new_book.id,
        "title": new_book.title,
        "author": new_book.author,
        "year": new_book.year
    }


@app.get("/books/")
def get_all_books(db: Session = Depends(get_db)):
    """Retrieve all books from the database."""
    books = db.query(Book).all()
    return [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "year": b.year
        }
        for b in books
    ]


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book by ID."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


@app.put("/books/{book_id}")
def update_book(book_id: int, book_data: dict, db: Session = Depends(get_db)):
    """Update a book's details."""
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if "title" in book_data:
        book.title = book_data["title"]
    if "author" in book_data:
        book.author = book_data["author"]
    if "year" in book_data:
        book.year = book_data["year"]
    
    db.commit()
    db.refresh(book)
    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "year": book.year
    }


@app.get("/books/search/")
def search_books(
    title: str = None,
    author: str = None,
    year: int = None,
    db: Session = Depends(get_db)
):
    """Search books by title, author, or year."""
    query = db.query(Book)
    
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)
    
    books = query.all()
    return [
        {
            "id": b.id,
            "title": b.title,
            "author": b.author,
            "year": b.year
        }
        for b in books
    ]
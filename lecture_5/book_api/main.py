from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

# imports
import models
from database import engine, get_db
from schemas import BookCreate, BookUpdate, BookResponse

# create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# create app instance
app = FastAPI(
    title="Book Collection API",
    description="Homework project for web frameworks",
    version="1.0"
)


@app.get("/")
async def root():
    """Root endpoint - shows available routes."""
    return {
        "message": "Book API is running",
        "docs": "Go to /docs for interactive testing",
        "endpoints": [
            "POST /books/ - add book",
            "GET /books/ - list all books",
            "GET /books/{id} - get one book",
            "PUT /books/{id} - update book",
            "DELETE /books/{id} - delete book",
            "GET /books/search/ - search books"
        ]
    }


@app.post("/books/", response_model=BookResponse, status_code=201)
async def create_book(
    book: BookCreate, 
    db: Session = Depends(get_db)
) -> BookResponse:
    """
    Add a new book to the collection.
    
    Args:
        book: Book data (title, author, year)
        db: Database session
        
    Returns:
        BookResponse: The created book with ID
        
    Raises:
        HTTPException: If book already exists (by title+author)
    """
    # check if book already exists
    existing = db.query(models.Book).filter(
        models.Book.title == book.title,
        models.Book.author == book.author
    ).first()
    
    if existing:
        raise HTTPException(400, "Book already exists in collection")
    
    # create new book
    new_book = models.Book(
        title=book.title,
        author=book.author,
        year=book.year
    )
    
    db.add(new_book)
    db.commit()
    db.refresh(new_book)  # get the id from db
    
    return new_book


@app.get("/books/", response_model=List[BookResponse])
async def get_all_books(
    skip: int = Query(0, ge=0, description="Skip N books (for pagination)"),
    limit: int = Query(100, ge=1, le=100, description="Max books to return"),
    db: Session = Depends(get_db)
) -> List[BookResponse]:
    """
    Get all books with optional pagination.
    
    Args:
        skip: How many books to skip (default 0)
        limit: Max books to return (default 100, max 100)
        db: Database session
        
    Returns:
        List[BookResponse]: List of all books
    """
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books


@app.get("/books/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int, 
    db: Session = Depends(get_db)
) -> BookResponse:
    """
    Get a single book by ID.
    
    Args:
        book_id: ID of the book to get
        db: Database session
        
    Returns:
        BookResponse: The book if found
        
    Raises:
        HTTPException: If book not found (404)
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book:
        raise HTTPException(404, f"Book with ID {book_id} not found")
    
    return book


@app.put("/books/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_db)
) -> BookResponse:
    """
    Update a book's information.
    
    Args:
        book_id: ID of book to update
        book_update: Fields to update (title, author, year)
        db: Database session
        
    Returns:
        BookResponse: Updated book
        
    Raises:
        HTTPException: If book not found (404)
    """
    # find the book first
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book:
        raise HTTPException(404, f"Book with ID {book_id} not found")
    
    # update only provided fields
    update_data = book_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(book, field, value)  # updates the field
    
    db.commit()
    db.refresh(book)
    
    return book


@app.delete("/books/{book_id}")
async def delete_book(
    book_id: int, 
    db: Session = Depends(get_db)
) -> dict:
    """
    Delete a book from the collection.
    
    Args:
        book_id: ID of book to delete
        db: Database session
        
    Returns:
        dict: Success message and deleted book info
        
    Raises:
        HTTPException: If book not found (404)
    """
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if not book:
        raise HTTPException(404, f"Book with ID {book_id} not found")
    
    # store info before deleting
    book_info = {
        "id": book.id,
        "title": book.title,
        "author": book.author
    }
    
    db.delete(book)
    db.commit()
    
    return {
        "message": f"Book '{book.title}' deleted",
        "deleted_book": book_info
    }


@app.get("/books/search/", response_model=List[BookResponse])
async def search_books(
    title: Optional[str] = Query(None, description="Search by title (partial match)"),
    author: Optional[str] = Query(None, description="Search by author (partial match)"),
    year: Optional[int] = Query(None, description="Search by exact year"),
    db: Session = Depends(get_db)
) -> List[BookResponse]:
    """
    Search books by title, author, or year.
    
    Args:
        title: Search term for title (case-insensitive)
        author: Search term for author (case-insensitive)
        year: Exact year to match
        db: Database session
        
    Returns:
        List[BookResponse]: Matching books
    """
    query = db.query(models.Book)
    
    # build query based on what's provided
    if title:
        query = query.filter(models.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(models.Book.year == year)
    
    books = query.all()
    return books


@app.get("/books/stats/count")
async def get_book_count(db: Session = Depends(get_db)) -> dict:
    """
    Get total number of books in collection.
    
    Args:
        db: Database session
        
    Returns:
        dict: Count of books
    """
    count = db.query(models.Book).count()
    return {"total_books": count, "message": f"There are {count} books"}
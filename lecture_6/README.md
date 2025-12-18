# Book Collection API (Dockerized)

A FastAPI application for managing a book collection, now containerized with Docker.

## Features
- Add, view, update, and delete books
- Search books by title, author, or year
- SQLite database with SQLAlchemy ORM
- Health check endpoint (`/healthcheck`)
- Fully Dockerized deployment

## Quick Start

### **Option 1: Docker (Recommended)**
```bash
# Build the Docker image
docker build . -t book-api:latest

# Run the container
docker run -d -p 8000:8000 --name book-api-container book-api:latest

# Check if it's running
curl http://localhost:8000/healthcheck
# Should return: {"status":"ok"}
```

### Option 2: Traditional Setup
```bash

# 1. Install dependencies
pip install -r requirements.txt

# 2. Initialize database (creates books.db)
python -c "from models import Base, engine; Base.metadata.create_all(bind=engine)"

# 3. Run the application
uvicorn main:app --reload
```

Project Structure:
lecture_6/
├── Dockerfile         
├── main.py            
├── models.py          
├── requirements.txt   
├── README.md          
└── books.db           
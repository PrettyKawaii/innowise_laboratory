# Book Collection API (Dockerized)

## Setup

### **Option 1: via Docker (Recommended)**
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

1. pip install -r requirements.txt
2. Run: uvicorn main:app --reload
3. Open: http://127.0.0.1:8000/healthcheck
```

## Project Structure:
lecture_6/
├── Dockerfile         
├── main.py            
├── models.py          
├── requirements.txt   
├── README.md          
└── books.db    

## Features
- Add, view, update, delete books
- Search by title/author/year
- SQLite database
- FastAPI with SQLAlchemy ORM
- Health check endpoint (`/healthcheck`)
- Fully Dockerized deployment

       
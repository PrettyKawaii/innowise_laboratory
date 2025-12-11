from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    """Book model for the database table."""
    __tablename__ = "books"  # table name in db
    
    id = Column(Integer, primary_key=True, index=True)  # auto increment id
    title = Column(String, nullable=False)  # can't be null
    author = Column(String, nullable=False)  # required
    year = Column(Integer, nullable=True)  # optional year
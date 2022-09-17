import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

# model/table
class Student(Base):
    __tablename__ = "Student"

    # fields
    id = Column(Integer,primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer)
    borrow_book = relationship("Borrow_book", backref="Student")

class Book(Base):
    __tablename__ = "Book"

    # fields
    book_id = Column(Integer,primary_key=True, index=True)
    title = Column(String(20))
    author = Column(String(20))
    total_copies = Column(Integer)
    borrow_book = relationship("Borrow_book",backref = "Book")

class Borrow_book(Base):
    __tablename__ = "borrow_book"

    stud_id = Column(Integer,ForeignKey('Student.id'))
    book_id = Column(Integer,ForeignKey('Book.book_id'))
    issued_date = Column(datetime.date.today())

class Return_book(Base):
    __tablename__ = "return_book"

    stud_id = Column(Integer, ForeignKey('Student.id'))
    book_id = Column(Integer, ForeignKey('Book.book_id'))
    return_date = Column(datetime.date.today())



class inventory(Base):
    __tablename__ = "inventory"



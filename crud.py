from sqlalchemy.orm import Session

from models import Student,Book

def create_student(db:Session, first_name, last_name, age):
    new_stud = Student(first_name=first_name,last_name=last_name,age=age)
    db.add(new_stud)
    db.commit()
    db.refresh(new_stud)
    return new_stud

def get_stud(db:Session, id:int):
    db_stud = db.query(Student).filter(Student.id==id).first()
    return db_stud

def list_student_all(db:Session):
    all_stud = db.query(Student).all()
    return all_stud

def add_book(db:Session, title,author,total_copies):
    new_book = Book(title=title,author=author,total_copies=total_copies)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def book_list(db:Session):
    all_books = db.query(Book).all()
    return all_books



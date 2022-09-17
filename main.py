from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

import models
import crud
from db import engine
from db import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

#initailize FastApi instance
app = FastAPI()

#define endpoint
@app.get("/")
def home():
    return {"Ahoy": "Captain"}

@app.post("/create_stud")
def create_stud(first_name:str, last_name:str, age:int, db:Session = Depends(get_db)):
    student = crud.create_student(db=db,first_name=first_name,last_name=last_name,age=age)
    return {"Student":student}

@app.get("/get_student/{id}/")
def get_student(id:int,db:Session=Depends(get_db)):
    student = crud.get_stud(db=db,id=id)
    return student

@app.post("/add_book")
def add_book(title:str,author:str,total_copies:int,db:Session = Depends(get_db)):
    book = crud.add_book(db=db,title=title,author=author,total_copies=total_copies)
    return f"Book is successfully added!! {book}"

@app.get("/get_all_books")
def get_all_books(db:Session=Depends(get_db)):
    book = crud.book_list(db=db)
    return book


from fastapi import FastAPI,Request ,Form
from fastapi.templating import Jinja2Templates
import sqlite3
from pydantic import BaseModel ,Field
from fastapi.responses import RedirectResponse
app = FastAPI()
templates = Jinja2Templates(directory="templates")
class Student(BaseModel):
    name:str = Field(max_length=50)
    age:int  = Field(ge=18,le=60)
    gender:str 
    marks:int = Field(le=100)
    course:str = Field(max_length=20)
    image:str
    status:int

def get_connection():

    connection = sqlite3.connect(
        "student.db"
    )
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    query = """ 

            CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            marks INTEGER,
            course TEXT,
            image TEXT,
            status INTEGER
            )
            """
    cursor.execute(query)
    connection.commit()
    connection.close()
create_table()


@app.get("/")
def home(req:Request):
    connecton = get_connection()
    cursor = connecton.cursor()
    query = "select * from student"
    cursor.execute(query)
    students = cursor.fetchall()
    connecton.close()
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={
            "stds":students
        }
    )

@app.get("/student/add")
def send_form(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="student_form.html",
        context={}
    )


@app.post("/student/add")
def add_details(
    name = Form(),
    age = Form(),
    gender = Form(),
    marks = Form(),
    course = Form(),
    image = Form(),
    status = Form()

):
    std_obj = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    values = (std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status)
    connection = get_connection()
    cursor = connection.cursor()
    query = """INSERT INTO STUDENT (name,age,gender,marks,course,image,status) values(?,?,?,?,?,?,?)"""
    cursor.execute(query,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/" , status_code=303)


@app.get("/{std_id}")
def single_std_details(req:Request,std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    query = "select * from student where id = ?"
    cursor.execute(query,(std_id,))
    single_student_details = cursor.fetchone()
    connection.close
    return templates.TemplateResponse(
        request=req,
        name="single_std.html",
        context={
            "std":single_student_details
        }
    )

@app.post("/std/{std_id}")
def delete_std_by_id(std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    query = "delete from student where id = ?"
    cursor.execute(query,(std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/" , status_code=303)

@app.get("/student/edit/{std_id}")
def edit_std_by_id(req:Request,std_id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "select * from student where id = ?"
    cursor.execute(query,(std_id,))
    student_for_edit = cursor.fetchone()
    connection.close()
    print(student_for_edit)
    print(student_for_edit[1])
    return templates.TemplateResponse(
        request=req,
        name= "edit_std.html",
        context={
            "std":student_for_edit,
            "s_n":student_for_edit[1]
        }
    )

@app.post("/student/edit/{std_id}")
def update_details(req:Request,std_id,
                   name = Form(),
                   age = Form(),
                   gender = Form(),
                   marks = Form(),
                   course = Form(),
                   image = Form(),
                   status = Form()):
    std_obj = Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    connection = get_connection()
    cursor = connection.cursor()
    query = """
            update student 
            set
            name = ?,
            age = ?,
            gender = ?,
            marks = ?,
            course = ?,
            image = ?,
            status = ?
            where id = ? """
    cursor.execute(query,(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,std_obj.status,std_id))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/" , status_code=303)

# 🎓 Student Management System

## 📌 Project Overview

The **Student Management System** is a web-based application developed using Python FastAPI and SQLite. It helps users efficiently manage student information through a simple and user-friendly interface.

The application supports CRUD operations (Create, Read, Update, Delete), allowing users to add, view, update, and delete student records.

## 🚀 Features

- ➕ Add new student details.
- 📋 View all registered students.
- 🔍 View individual student information.
- ✏️ Update existing student records.
- 🗑️ Delete student records.
- 📊 Store student marks and course details.
- 👤 Manage student gender and age information.
- 🖼️ Store student image paths.
- 📅 Track attendance status (Present/Absent).
- ✅ Validate input data using Pydantic.

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| Python | Backend programming language |
| FastAPI | Backend web framework |
| SQLite | Database |
| Pydantic | Data validation |
| HTML5 | Frontend structure |
| CSS3 | Frontend styling |
| Jinja2 | Template rendering |

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
│
├── student.db
│
├── templates/
│   ├── home.html
│   ├── student_form.html
│   ├── single_std.html
│   └── edit_std.html
│
└── README.md
```

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Navigate to Project Directory

```bash
cd Student-Management-System
```

### Step 3: Install Required Packages

```bash
pip install fastapi uvicorn jinja2 python-multipart
```

### Step 4: Run the Application

```bash
uvicorn main:app --reload
```

### Step 5: Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## 🔄 CRUD Operations

| Operation | Description |
|---|---|
| Create | Add new student details |
| Read | Display student records |
| Update | Modify existing student details |
| Delete | Remove student records |

## 📚 Data Validation

Pydantic is used to validate student information.

- Student name: Maximum 50 characters.
- Age: Between 18 and 60.
- Marks: Maximum 100.
- Course: Maximum 20 characters.

## 🎯 Project Objective

The main objective of this project is to simplify student record management and gain practical experience in Python backend development, database connectivity, web application development, and CRUD operations.

## 👨‍💻 Author

**Uma**

Python Developer | Backend Development Enthusiast

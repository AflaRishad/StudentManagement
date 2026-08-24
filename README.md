# Student Management System

A console-based application for managing student records using **Python** and **Microsoft SQL Server**.

The project follows a layered architecture:

**Database → Repository → Service → UI**

This provides clear separation of concerns, modularity, and dependency injection.

## Features

* Add a new student
* View all students
* Search for a student by ID
* Update student details
* Delete a student with confirmation
* Input validation
* Exception handling

## Technologies Used

* **Python 3.x**
* **pyodbc** – Python library for connecting to SQL Server
* **Microsoft SQL Server Express**
* **ODBC Driver 17 for SQL Server**
* **SQL**
* **Object-Oriented Programming (OOP)**
* **Dependency Injection**
* **Repository Pattern**
* **Service Layer Architecture**

## Project Structure

```text
StudentManagement/
│
├── main.py
├── database.py
├── student.py
├── student_repository.py
├── student_service.py
└── README.md
```

### File Responsibilities

**main.py**

* Entry point of the application
* Displays the console menu
* Accepts user input
* Calls the service layer

**database.py**

* Creates and manages the SQL Server database connection

**student.py**

* Contains the `Student` class
* Acts as the data model/DTO

**student_repository.py**

* Executes SQL queries
* Performs CRUD operations
* Converts database rows into `Student` objects

**student_service.py**

* Contains business logic
* Validates input
* Coordinates operations between the UI and repository

## Database Setup

Create the database and table in SQL Server:

```sql
CREATE DATABASE StudentManagement;
GO

USE StudentManagement;
GO

CREATE TABLE Students (
    StudentId INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(100) NOT NULL,
    Age INT NOT NULL,
    Course NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) NOT NULL
);
GO
```

### Database Columns

| Column    | Data Type     | Description                                |
| --------- | ------------- | ------------------------------------------ |
| StudentId | INT           | Primary key and automatically generated ID |
| Name      | NVARCHAR(100) | Student's name                             |
| Age       | INT           | Student's age                              |
| Course    | NVARCHAR(100) | Student's course                           |
| Email     | NVARCHAR(100) | Student's email                            |

## Installation

### 1. Install Python

Python 3.7 or later is required.

### 2. Install pyodbc

```bash
pip install pyodbc
```

### 3. Install SQL Server

Microsoft SQL Server Express can be used for development.

### 4. Install ODBC Driver

The application uses the **ODBC Driver 17 for SQL Server**.

## Database Connection

The application uses a connection string similar to:

```python
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=StudentManagement;"
    "Trusted_Connection=yes;"
)
```

The default configuration uses:

* **Server:** `.\SQLEXPRESS`
* **Database:** `StudentManagement`
* **Authentication:** Windows Authentication

If a different SQL Server instance or authentication method is used, the connection string can be modified.

## Running the Application

Open the project folder in the terminal and run:

```bash
python main.py
```

The application displays the following menu:

```text
===================================
       STUDENT MANAGEMENT SYSTEM
===================================

Please choose an option:

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

===================================
```

The user selects an option by entering the corresponding number.

## CRUD Operations

### Create

Adds a new student to the `Students` table.

Example:

```text
Name: John Doe
Age: 22
Course: Computer Science
Email: john.doe@example.com
```

### Read

Displays all students stored in the database or searches for a particular student using their ID.

### Update

Allows the user to modify existing student information such as:

* Name
* Age
* Course
* Email

### Delete

Deletes a student after asking the user for confirmation.

## Architecture

### 1. Database Layer

Responsible for establishing and managing the connection to SQL Server.

```text
Application
     ↓
Database Connection
     ↓
SQL Server
```

### 2. Repository Layer

The repository layer communicates directly with the database.

It contains SQL queries for:

* INSERT
* SELECT
* UPDATE
* DELETE

The repository hides database implementation details from the service layer.

### 3. Service Layer

The service layer contains the application's business logic.

It:

* Validates input
* Checks required values
* Coordinates operations
* Calls repository methods

### 4. UI Layer

The `main.py` file acts as the user interface.

It:

* Displays the menu
* Gets input from the user
* Calls the service layer
* Displays results and error messages

## Dependency Injection

Dependencies are created in `main.py` and passed down to the required classes.

For example:

```text
main.py
   ↓
StudentService
   ↓
StudentRepository
   ↓
Database
   ↓
SQL Server
```

This is an example of **Dependency Injection** because classes receive the objects they depend on instead of creating those dependencies internally.

It makes the application easier to:

* Test
* Maintain
* Modify
* Extend

## Error Handling and Validation

The application validates user input and handles errors such as:

* Invalid student ID
* Invalid age
* Empty name
* Empty course
* Invalid email
* Student not found
* Database connection errors
* SQL errors
* Invalid menu choices

The application is designed so that invalid input does not cause the program to crash.

## Example

A user can add:

```text
Name: John Doe
Age: 22
Course: Computer Science
Email: john.doe@example.com
```

The information is stored in SQL Server and can later be viewed, searched, updated, or deleted through the console menu.

## Key Concepts Demonstrated

This project demonstrates practical use of:

* Python
* OOP
* Classes and objects
* Constructors
* Encapsulation
* SQL
* SQL Server
* Database connectivity
* CRUD operations
* `pyodbc`
* Exception handling
* Input validation
* Dependency Injection
* Repository Pattern
* Service Layer
* Layered Architecture
* Separation of Concerns

## Conclusion

The Student Management System is a **console-based Python application**, not a web application.

It uses **Python as the application/programming layer** and **Microsoft SQL Server as the database layer**. The layered architecture separates database operations, business logic, and user interaction, making the application modular and easier to maintain.

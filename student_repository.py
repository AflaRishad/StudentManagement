# Database provides SQL Server connections.
from database import Database
# Student represents database rows in Python.
from student import Student


class StudentRepository:

    def __init__(self, database):
        # Receive the database dependency from the application.
        self.database = database

    def add_student(self, student):

        # Create a connection and cursor for this operation.
        connection = self.database.connect()
        cursor = connection.cursor()

        query = """
            INSERT INTO Students (Name, Age, Course, Email)
            VALUES (?, ?, ?, ?)
        """

        # ? placeholders keep values separate from the SQL command.
        cursor.execute(
            query,
            student.name,
            student.age,
            student.course,
            student.email
        )

        # Save the inserted record permanently.
        connection.commit()

        # Release database resources after use.
        cursor.close()
        connection.close()

    def get_all_students(self):

        # Query every student record.
        connection = self.database.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM Students"

        cursor.execute(query)

        rows = cursor.fetchall()

        # Convert each database row into a Student object.
        students = []

        for row in rows:
            student = Student(
                row.StudentId,
                row.Name,
                row.Age,
                row.Course,
                row.Email
            )

            students.append(student)

        cursor.close()
        connection.close()

        return students

    def get_student_by_id(self, student_id):

        # Find one student using the primary key.
        connection = self.database.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM Students WHERE StudentId = ?"

        cursor.execute(query, student_id)

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        # Return None when no matching record exists.
        if row is None:
            return None

        return Student(
            row.StudentId,
            row.Name,
            row.Age,
            row.Course,
            row.Email
        )

    def update_student(self, student):

        # Update the stored details for one student.
        connection = self.database.connect()
        cursor = connection.cursor()

        query = """
            UPDATE Students
            SET Name = ?,
                Age = ?,
                Course = ?,
                Email = ?
            WHERE StudentId = ?
        """

        cursor.execute(
            query,
            student.name,
            student.age,
            student.course,
            student.email,
            student.student_id
        )

        connection.commit()

        # rowcount shows whether a record was changed.
        rows_updated = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_updated > 0

    def delete_student(self, student_id):

        # Delete one student by ID.
        connection = self.database.connect()
        cursor = connection.cursor()

        query = "DELETE FROM Students WHERE StudentId = ?"

        cursor.execute(query, student_id)

        connection.commit()

        # rowcount shows whether a record was deleted.
        rows_deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return rows_deleted > 0
# Student stores the validated student details.
from student import Student


class StudentService:

    def __init__(self, repository):
        # Receive the repository used for database operations.
        self.repository = repository

    def add_student(self, name, age, course, email):

        # Validate user input before saving it.
        if not name.strip():
            raise ValueError("Name cannot be empty")

        if age <= 0:
            raise ValueError("Age must be greater than 0")

        if not course.strip():
            raise ValueError("Course cannot be empty")

        if not email.strip():
            raise ValueError("Email cannot be empty")

        # Build a new student; the database assigns its ID.
        student = Student(
            None,
            name,
            age,
            course,
            email
        )

        self.repository.add_student(student)

    def get_all_students(self):
        # Pass the read request to the repository.
        return self.repository.get_all_students()

    def get_student_by_id(self, student_id):

        # IDs must be positive database keys.
        if student_id <= 0:
            raise ValueError("Student ID must be greater than 0")

        return self.repository.get_student_by_id(student_id)

    def update_student(self, student_id, name, age, course, email):

        # Validate the ID and replacement values.
        if student_id <= 0:
            raise ValueError("Student ID must be greater than 0")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        if age <= 0:
            raise ValueError("Age must be greater than 0")

        if not course.strip():
            raise ValueError("Course cannot be empty")

        if not email.strip():
            raise ValueError("Email cannot be empty")

        # Build the replacement student object.
        student = Student(
            student_id,
            name,
            age,
            course,
            email
        )

        return self.repository.update_student(student)

    def delete_student(self, student_id):

        # Validate the ID before deleting anything.
        if student_id <= 0:
            raise ValueError("Student ID must be greater than 0")

        return self.repository.delete_student(student_id)
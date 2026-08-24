# Database manages the SQL Server connection.
from database import Database
# Repository performs SQL queries.
from student_repository import StudentRepository
# Service validates input and coordinates operations.
from student_service import StudentService


# Inject each dependency into the next application layer.
database = Database()
repository = StudentRepository(database)
service = StudentService(repository)


def display_student(student):
    # Print one student's details in a readable format.
    print(
        f"ID: {student.student_id} | "
        f"Name: {student.name} | "
        f"Age: {student.age} | "
        f"Course: {student.course} | "
        f"Email: {student.email}"
    )

 # Load and display every student.
def display_all_students():
   
    students = service.get_all_students()

    if not students:
        print("\nNo students found.")
        return

    print("\n--- STUDENTS ---")

    for student in students:
        display_student(student)

# Read and save details for a new student.
def add_student():
    
    print("\n--- ADD STUDENT ---")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")

    service.add_student(
        name,
        age,
        course,
        email
    )

    print("\nStudent added successfully.")

# Look up one student by ID.
def search_student():
    
    print("\n--- SEARCH STUDENT ---")

    student_id = int(input("Enter student ID: "))

    student = service.get_student_by_id(student_id)

    if student:
        display_student(student)
    else:
        print("\nStudent not found.")

# Find a student, then replace its details.
def update_student():
    
    print("\n--- UPDATE STUDENT ---")

    student_id = int(input("Enter student ID: "))

    # Check whether student exists
    existing_student = service.get_student_by_id(student_id)

    if not existing_student:
        print("\nStudent not found.")
        return

    print("\nEnter new student details:")

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    email = input("Enter new email: ")

    updated = service.update_student(
        student_id,
        name,
        age,
        course,
        email
    )

    if updated:
        print("\nStudent updated successfully.")
    else:
        print("\nStudent update failed.")

# Confirm before deleting the selected student.
def delete_student():
    
    print("\n--- DELETE STUDENT ---")

    student_id = int(input("Enter student ID: "))

    # Check whether student exists
    existing_student = service.get_student_by_id(student_id)

    if not existing_student:
        print("\nStudent not found.")
        return

    print("\nStudent found:")
    display_student(existing_student)

    confirmation = input(
        "\nAre you sure you want to delete this student? (y/n): "
    )

    if confirmation.lower() == "y":

        deleted = service.delete_student(student_id)

        if deleted:
            print("\nStudent deleted successfully.")
        else:
            print("\nStudent deletion failed.")

    else:
        print("\nDeletion cancelled.")


def menu():

    # Keep showing options until the user exits.
    while True:

        print("\n===================================")
        print("     STUDENT MANAGEMENT SYSTEM       ")
        print("=====================================")

        print("    ")
        print("Please choose an option:")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("   ")

        print("===================================")

        choice = input("Enter your choice: ")

        # Handle invalid numbers without stopping the program.
        try:

            if choice == "1":
                add_student()

            elif choice == "2":
                display_all_students()

            elif choice == "3":
                search_student()

            elif choice == "4":
                update_student()

            elif choice == "5":
                delete_student()

            elif choice == "6":
                print("\nThank you for using Student Management System!")
                break

            else:
                print("\nInvalid choice. Please enter a number from 1 to 6.")

        except ValueError as e:
            print(f"\nError: {e}")

        except Exception as e:
            print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    # Start the program only when this file is run directly.
    menu()
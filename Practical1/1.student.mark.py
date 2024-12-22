# Student Mark Management System using lists, dicts, and tuples

# Global variables
students = []  # List of tuples (id, name, DoB)
courses = []   # List of tuples (id, name)
marks = {}     # Dictionary: {course_id: {student_id: mark}}

# Input functions
def input_number_of_students():
    return int(input("Enter the number of students: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student Date of Birth (DoB): ")
    students.append((student_id, student_name, student_dob))

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses.append((course_id, course_name))

def input_marks_for_course():
    if not courses:
        print("No courses available. Please input course information first.")
        return

    course_id = input("Enter course ID to input marks for: ")
    if course_id not in [course[0] for course in courses]:
        print("Invalid course ID.")
        return

    # Initialize marks for the course if not already done
    if course_id not in marks:
        marks[course_id] = {}

    for student in students:
        student_id = student[0]
        mark = float(input(f"Enter mark for student {student_id} ({student[1]}): "))
        marks[course_id][student_id] = mark

# Listing functions
def list_courses():
    if not courses:
        print("No courses available.")
        return
    print("Courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students():
    if not students:
        print("No students available.")
        return
    print("Students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks():
    if not marks:
        print("No marks available.")
        return

    course_id = input("Enter course ID to view marks: ")
    if course_id not in marks:
        print("No marks available for this course.")
        return

    print(f"Marks for course {course_id}:")
    for student_id, mark in marks[course_id].items():
        student_name = next((s[1] for s in students if s[0] == student_id), "Unknown")
        print(f"Student {student_id} ({student_name}): {mark}")

# Main program
def main():
    print("Welcome to the Student Mark Management System!")
    
    # Input students
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_info()

    # Input courses
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_info()

    # Input marks
    while True:
        print("\nSelect an option:")
        print("1. Input marks for a course")
        print("2. List courses")
        print("3. List students")
        print("4. Show marks for a course")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            input_marks_for_course()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_student_marks()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

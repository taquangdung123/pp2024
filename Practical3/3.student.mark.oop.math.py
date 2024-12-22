import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name
        self.__gpa = 0.0

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def __str__(self):
        return f"Student[ID: {self.__student_id}, Name: {self.__name}, GPA: {self.__gpa:.2f}]"


class Course:
    def __init__(self, course_id, course_name, credits):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credits = credits

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"Course[ID: {self.__course_id}, Name: {self.__course_name}, Credits: {self.__credits}]"


class Marks:
    def __init__(self):
        self.__marks = {}

    def add_mark(self, student, course, mark):
        mark = math.floor(mark * 10) / 10  # Round down to 1 decimal place
        if student not in self.__marks:
            self.__marks[student] = {}
        self.__marks[student][course] = mark

    def get_mark(self, student, course):
        return self.__marks.get(student, {}).get(course, None)

    def list_marks(self):
        for student, courses in self.__marks.items():
            for course, mark in courses.items():
                print(f"{student.get_name()} in {course.get_course_name()} got {mark}")

    def calculate_gpa(self, student):
        courses = self.__marks.get(student, {})
        if not courses:
            return 0.0

        weights = np.array([course.get_credits() for course in courses])
        scores = np.array([self.__marks[student][course] for course in courses])
        gpa = np.sum(weights * scores) / np.sum(weights)
        return round(gpa, 2)


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Marks()

    def input_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)

    def input_course(self, course_id, course_name, credits):
        course = Course(course_id, course_name, credits)
        self.courses.append(course)

    def input_mark(self, student_id, course_id, mark):
        student = next((s for s in self.students if s.get_student_id() == student_id), None)
        course = next((c for c in self.courses if c.get_course_id() == course_id), None)
        if student and course:
            self.marks.add_mark(student, course, mark)

    def calculate_gpa_for_all(self):
        for student in self.students:
            gpa = self.marks.calculate_gpa(student)
            student.set_gpa(gpa)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda x: x.get_gpa(), reverse=True)

    def list_students(self):
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def list_marks(self):
        self.marks.list_marks()

    def run_ui(self):
        def ui(stdscr):
            stdscr.clear()
            stdscr.addstr("Welcome to the Student Management System!\n")
            stdscr.addstr("1. List Students\n")
            stdscr.addstr("2. List Courses\n")
            stdscr.addstr("3. List Marks\n")
            stdscr.addstr("4. Sort Students by GPA\n")
            stdscr.addstr("5. Exit\n")

            while True:
                stdscr.addstr("\nSelect an option: ")
                option = stdscr.getkey()

                if option == '1':
                    stdscr.clear()
                    stdscr.addstr("Students:\n")
                    for student in self.students:
                        stdscr.addstr(str(student) + "\n")
                elif option == '2':
                    stdscr.clear()
                    stdscr.addstr("Courses:\n")
                    for course in self.courses:
                        stdscr.addstr(str(course) + "\n")
                elif option == '3':
                    stdscr.clear()
                    stdscr.addstr("Marks:\n")
                    for student in self.students:
                        for course in self.courses:
                            mark = self.marks.get_mark(student, course)
                            if mark is not None:
                                stdscr.addstr(f"{student.get_name()} - {course.get_course_name()}: {mark}\n")
                elif option == '4':
                    self.calculate_gpa_for_all()
                    self.sort_students_by_gpa()
                    stdscr.clear()
                    stdscr.addstr("Students sorted by GPA:\n")
                    for student in self.students:
                        stdscr.addstr(str(student) + "\n")
                elif option == '5':
                    break
                else:
                    stdscr.addstr("Invalid option!\n")
                stdscr.refresh()

        curses.wrapper(ui)


# Example Usage
if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Input students
    sms.input_student(1, "Alice")
    sms.input_student(2, "Bob")

    # Input courses
    sms.input_course("MATH101", "Mathematics", 3)
    sms.input_course("PHYS101", "Physics", 4)

    # Input marks
    sms.input_mark(1, "MATH101", 89.45)
    sms.input_mark(1, "PHYS101", 92.75)
    sms.input_mark(2, "MATH101", 76.38)
    sms.input_mark(2, "PHYS101", 84.22)

    # Run UI
    sms.run_ui()

class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id  # Encapsulation
        self.__name = name

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Student[ID: {self.__student_id}, Name: {self.__name}]"


class Course:
    def __init__(self, course_id, course_name):
        self.__course_id = course_id  # Encapsulation
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name

    def __str__(self):
        return f"Course[ID: {self.__course_id}, Name: {self.__course_name}]"


class Marks:
    def __init__(self):
        self.__marks = {}  # Encapsulation

    def add_mark(self, student, course, mark):
        if student not in self.__marks:
            self.__marks[student] = {}
        self.__marks[student][course] = mark

    def get_mark(self, student, course):
        return self.__marks.get(student, {}).get(course, None)

    def list_marks(self):
        for student, courses in self.__marks.items():
            for course, mark in courses.items():
                print(f"{student.get_name()} in {course.get_course_name()} got {mark}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Marks()

    def input_student(self, student_id, name):
        student = Student(student_id, name)
        self.students.append(student)

    def input_course(self, course_id, course_name):
        course = Course(course_id, course_name)
        self.courses.append(course)

    def input_mark(self, student_id, course_id, mark):
        student = next((s for s in self.students if s.get_student_id() == student_id), None)
        course = next((c for c in self.courses if c.get_course_id() == course_id), None)
        if student and course:
            self.marks.add_mark(student, course, mark)

    def list_students(self):
        for student in self.students:
            print(student)

    def list_courses(self):
        for course in self.courses:
            print(course)

    def list_marks(self):
        self.marks.list_marks()


# Example Usage
if __name__ == "__main__":
    sms = StudentManagementSystem()

    # Input students
    sms.input_student(1, "Alice")
    sms.input_student(2, "Bob")

    # Input courses
    sms.input_course("MATH101", "Mathematics")
    sms.input_course("PHYS101", "Physics")

    # Input marks
    sms.input_mark(1, "MATH101", 95)
    sms.input_mark(2, "PHYS101", 89)

    # List all students, courses, and marks
    print("Students:")
    sms.list_students()
    print("\nCourses:")
    sms.list_courses()
    print("\nMarks:")
    sms.list_marks()

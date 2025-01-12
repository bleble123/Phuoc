class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def get_id(self):
        return self.__student.id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def display(self):
        print(f"ID: {self.__student.id}, Name: {self.__student.name}, DOB: {self.__student.dob}")

class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def get_id(self):
        return self.__course_id

    def get_name(self):
        return self.__name

    def display(self):
        print(f"ID: {self.__course_id}, Name: {self.__name}")

class MarkManager:
    def __init__(self):
        self.__marks = {}

    def input_mark(self, students, courses):
        course_id = input("Enter the course ID to input marks: ")

        course = None
        for c in courses:
            if c.get_id() == course_id:
                course = c
                break

        if not course:
            print("Course not found.")
            return
        
        for student in students:
            while True:
                try:
                    mark = float(input(f"Enter the mark for {student.get_name()} (ID: {student.get_id()}): "))

                    if 0 <= mark <= 100:
                        if student.get_id() not in self.__marks:
                            self.__marks[student.get_id()] = {}
                        self.__marks[student.get_id()][course_id] = mark
                        break
                    else:
                        print("Invalid mark.")
                except ValueError:
                    print("Invalid input.")

    def show_marks(self, students, courses):
        course_id = input("Enter the course ID to show marks: ")

        course = None
        for c in courses:
            if c.get_id() == course_id:
                course = c
                break

        if not course:
            print("Course not found.")
            return

        print("Marks for couse:")
        for student in students:
            mark = self.__marks.get(student.get_id(), {}).get(course_id, "No mark available")
            print(f"{student.get_name()} (ID: {student.get_id()}): {mark}")



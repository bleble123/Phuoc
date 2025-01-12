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


   


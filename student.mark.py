def main():
    students = []
    courses = []
    marks = {}
    
    while True:
        print("Options:")
        print("1. Input the number of students and their details")
        print("2. Input the number of courses and their details")
        print("3. Show list of students")
        print("4. Show list of courses")
        print("5. Input mark of students in the course.")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again")
            continue
        else:    
            if choice == 1:
                student_count = number_of_student()
                for i in range(student_count):
                    students.append(student_information())
            elif choice == 2:
                course_count = number_of_course()
                for i in range(course_count):
                    courses.append(course_information())
            elif choice == 3:
                print("\nStudents: ")
                list_student(students)
            elif choice == 4:
                print("\nCourse: ")
                list_course(courses)
            elif choice == 5:
                input_mark(students, courses, marks)
            else:
                print("Exiting the program.")
                break
        
        
def number_of_student():
    while True:
        try:
            return int(input("Enter the number of student in the course: "))
        except ValueError:
            print("Please try again")

def number_of_course():
    while True:
        try:    
            return int(input("Enter the number of courses: "))
        except ValueError:
            print("Please try again")
            
def student_information():
    student = {}
    student['id'] = input("Enter the id of the student: ")
    student['name'] = input("Enter the name of the student: ")
    student['dob'] = input("Enter the DOB of the student(DD/MM/YY): ")
    return student

def course_information():
    course = {}
    course['name'] = input("Enter the name of the course: ")
    course['id'] = input("Enter the id of the course: ")
    return course
 
def list_student(students):
    if not students:
        print("No student is available.")
    else:
        for i in students:
            print(f"ID: {i['id']}, Name: {i['name']}, DOB: {i['dob']}")
            
def list_course(courses):
    if not courses:
           print("No course available.")
    else:
        for i in courses:
            print(f"ID: {i['id']}, Name: {i['name']}")

def input_mark(students, courses, marks):
    course_id = input("Enter the course ID to input mark: ")
    
    course = None
    for c in courses:
        if c['id'] == course_id:
            course = c
            break
    
    if course is None:
        print("Course not found.")
        return
    
    for i in students:
        while True:
            try:
                mark = int(input(f"Enter the mark for student {i['name']} with ID {i['id']}: "))
                if mark < 0 or mark > 100:
                    print("Invalid mark for student.")
                if i['id'] not in marks:
                    marks[i['id']] = {}
                marks[i['id']][course['id']] = mark
                break
            except ValueError:
                print("Invalid mark. Please enter a valid number")    
    
if __name__ == "__main__":
    main()
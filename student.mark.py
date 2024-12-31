def main():
    students = []
    courses = []
    
    while True:
        print("\nOptions:")
        print("1. Input the number of students and their details")
        print("2. Input the number of courses and their details")
        print("3. Show list of students")
        print("4. Show list of courses")
        print("5. Exit")
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

if __name__ == "__main__":
    main()
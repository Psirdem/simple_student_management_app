# creating a student class
class Student:
    def __init__(self, name) -> None:
        self.name = name
        self.marks = []


# add student data

def add_stud_info():
    name = input("please what is your name: ")
    marks = input(
        "Please enter your results seperating them with a comma:\n ...  ")
    if len(marks) != 0:
        students_data = Student(name)
        Student.marks = [int(mark) for mark in marks.split(",")]
        return students_data
    else:
        Student.marks = []
    students_data = Student(name)

    return students_data


# method to add student marks to student data


def add_std_marks(students, mark):
    Student.marks.append(mark)


# compute the avarage mark of the student
def calculate_stud_average_mark(students):
    marks = Student.mark
    if len(marks) == 0:
        return 0
    else:
        return sum(marks)/len(marks)

# function for printing student records


def print_stud_details(students):
    print("Name : {}, Average mark {} ".format(
        Student.name, calculate_stud_average_mark(students)))

# function for printing list of students


def print_std_list(students_list):
    for id, student in enumerate(students_list):
        print("ID: {}".format(id))
        print_stud_details(student)

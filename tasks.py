# creating a student class
class Student:
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks


# add student data

def add_stud_info():
    name = input("please what is your name: ")
    marks = input(
        "Please enter your results seperating them with a comma:\n ...  ")
    if len(marks) != 0:
        marks = [int(mark) for mark in marks.split(",")]
    else:
        marks = []
    students_data = Student(name, marks)
    print(students_data.marks)
    return students_data


# method to add student marks to student data


def add_std_marks(students, mark):
    students.marks.append(mark)


# compute the avarage mark of the student
def calculate_stud_average_mark(students):
    marks = students.marks
    # print(marks)
    if len(marks) == 0:
        return 0
    else:
        return sum(marks)/len(marks)

# function for printing student records


def print_stud_details(students):
    print("Name : {}, Average mark {} ".format(
        students.name, calculate_stud_average_mark(students)))

# function for printing list of students


def print_std_list(students_list):
    for id, student in enumerate(students_list):
        print("ID: {}".format(id))
        print_stud_details(student)

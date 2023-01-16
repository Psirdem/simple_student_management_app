# this app is to help teachers to get the names of the students, with their marks as well as compute the avarage of their marks
students_list = []  # empty student list for student dictionary
# add student data


def add_stud_info():
    name = input("please what is your name: ")
    marks = input(
        "Please enter your results seperating them with a comma:\n ...  ")
    if len(marks) != 0:
        marks = [int(mark) for mark in marks.split(",")]
    else:
        marks = []
    students = {
        'name': name,
        'marks': marks
    }
    return students


# method to add student marks to student data
def add_std_marks(students, mark):
    students["marks"].append(mark)


# compute the avarage mark of the student
def calculate_stud_average_mark(students):
    marks = students["marks"]
    if len(marks) == 0:
        return 0
    else:
        return sum(marks)/len(marks)

# function for printing student records


def print_stud_details(students):
    print("Name : {}, Average mark {} ".format(
        students["Name"], calculate_stud_average_mark(students)))

# function for printing list of students


def print_std_list(students_list):
    for student in students_list:
        print_stud_details(student)


# USer menu
print("\n\nWelcome to the Students Continuous assesment app")
selection = 0
while selection in (0, 1, 2, 3):
    print("\n Please What would you like to do ?\n 1. Print Student List \n 2. Add a New student Record \n 3. Add a Mark to a Student \n 4. Quit\n")
    selection = int(input("Please Enter your response:.... "))

    if selection == 1:
        print("Getting all the list of students in the database...\n")
        if len(students_list) == 0:
            print("There are no student records in the database... try adding some...")
        else:
            print_std_list(students_list)

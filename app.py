# this app is to help teachers to get the names of the students, with their marks as well as compute the avarage of their marks
from tasks import *

students_list = []  # empty student list for student dictionary

# USer menu


def user_menu():
    print("\n\nWelcome to the Students Continuous assesment app")
    selection = 0
    while selection in (0, 1, 2, 3):
        print("\n Please What would you like to do ?\n 1. Print Student List \n 2. Add a New student Record \n 3. Add a Mark to a Student \n 4. Quit\n")
        selection = int(input("Please Enter your response:.... "))

        if selection == 1:
            print("Getting all the list of students in the database...\n")
            if len(students_list) == 0:
                print(
                    "There are no student records in the database... try adding some...")
            else:
                print_std_list(students_list)
        elif selection == 2:
            print("Adding a new student Record to database....")
            students_list.append(add_stud_info())
            print("Record Added...")

        elif selection == 3:
            if len(students_list) == 0:
                print(
                    "Sorry there are no student records in the database.... Try adding some...")
            else:
                print("Adding mark a student record...")
                id = int(
                    input("What is the ID of the student whose mark you want to add?... "))
                mark = float(input("Enter the mark you want to add... "))
                students_list[id].add_mark(mark)
                print("Mark added successfully...")


user_menu()

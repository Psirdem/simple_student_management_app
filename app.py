def create_student():
    name = input('What is your name?: ')
    student_data = {
        'name': name,
        'marks': []
    }
    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)
    return student
# print(create_student())


student = create_student()
print(add_mark(student, 5))

num_list = []
for num in range(10):
    num_list.append(num)

print(num_list)

[num_list.append(num) for num in range(50)]
print(num_list)

# Get data of a certain number of students from the user and store them in a JSON file.

import json

student_number = int(input("Enter the number of students: "))
count = 0 

students = []

while count < student_number:
    name = input("Enter the name of the student: ")
    average = input("Enter the average of the student: ")

    student = {}
    student['name'] = name 
    student['average'] = average

    students.append(student)

    count += 1

with open('students.json', 'w') as f:
    f.write(json.dumps(students))

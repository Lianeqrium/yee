# Sarah Sides
# 7/10/18
# Student Database

import time

done = 1
want_to_view = 3
student_list = []

while done == 1:

    student_data = []
    
    name = input("What is the name of the student? ")
    year = int(input("What grade year is the student currently in? Please enter a number. "))
    grade = int (input("What is the number grade of the student? Please enter a number. "))
    comment = input("Do you have any other comments about the student? ")
    done = int (input("Would you like to add another student? 1 - yes 2 - no "))

    student_data.append(name)
    student_data.append(year)
    student_data.append(grade)
    student_data.append(comment)

    student_list.append(student_data)

if done == 2:
    want_to_view = int(input ("Would you like to view the list of students? 1 - yes 2 - no "))

if want_to_view == 1:
    for student in student_list:
        print (student)

    time.sleep(1)
    print ()
    print ("Thank you! Have a nice day!")
    
if want_to_view == 2:
    print ("Thank you! Have a nice day!")
    


'''
# Get and print the 2 marks each for 3 students. Also, get each studen't name
# output should be
# Mark 1 for Student 1 is 55
# Mark 2 for Student 1 is 67
# Mark 1 for Student 2 is 56 
#etc

for student in range (#FillinMissingCode):
    #FillinMissingCode  to get studnet name
    for mark in range (#FillinMissingCode):
        inputMark = float (input(f"#FillinMissingCode")) #use formatted string
        print (#FillinMissingCode)
'''
# Get the number of students
num_students = int(input("Enter the number of students: "))

# Loop through each student
for student in range(1, num_students + 1):
    student_name = input(f"Enter the name of Student {student}: ")

    # Loop through each mark (Assuming two marks per student)
    for mark_number in range(1, 3):
        input_mark = float(input(f"Enter Mark {mark_number} for {student_name}: "))
        print(f"Mark {mark_number} for {student_name} is {input_mark}")

'''#same problem as above, but output should have the student name and all the marks in the same line.
# Eg - Input - Student Name - Chitra, Mark1 1 55, Mark 2 67
#output -  Chitra's marks 55, 67'''

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Initialize a list to store student information
student_info = []

# Loop through each student
for student in range(1, num_students + 1):
    student_name = input(f"Enter the name of Student {student}: ")

    # Initialize a list to store the marks for this student
    marks = []

    # Loop through each mark (Assuming two marks per student)
    for mark_number in range(1, 3):
        input_mark = float(input(f"Enter Mark {mark_number} for {student_name}: "))
        marks.append(input_mark)

    # Add the student's name and marks to the student_info list
    student_info.append((student_name, marks))

# Print the student information join function
for student_name, marks in student_info:
    marks_str = ', '.join(map(str, marks))
    print(f"{student_name}'s marks: {marks_str}")


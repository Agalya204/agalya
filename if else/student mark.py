#Calculate the Grade for a student, using 3 marks.
# The student has 100 marks in any one subject, Grade is A.
# if the student has 90 or above in any one subject  Grade is B
# if the student has 60 or above in any one subject  Grade is C
# if the student has 50 or less  in all subjects  Grade is F, otherwise Grade is D.

mark1 = int(input("Enter subject 1 mark:")) # Fill in the student's marks for  subject 1
mark2 = int(input("Enter subject 2 mark:")) # Fill in the student's marks for subject 2
mark3 = int(input("Enter subject 3 mark:")) # Fill in the student's marks for subject 3

if mark1 == 100 or mark2 == 100 or mark3 == 100:
    grade = "A"
elif mark1 >= 90 or mark2 >= 90 or mark3 >= 90:
    grade = "B"
elif mark1 >= 60 or mark2 >= 60 or mark3 >= 60:
    grade = "C"
elif mark1 <= 50 and mark2 <= 50 and mark3 <= 50:
    grade = "F"
else:
    grade = "D"

print("The student's grade is:", grade)

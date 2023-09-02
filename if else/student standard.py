# Problem 6: Calculate and print which standard the student is studying

# Ask the user for his/her name and print 'Hello', user's name.
user_name = input("Hello, what is your name? ")

# Ask what year they were born.
birth_year = int(input(f"Hello {user_name}, what year were you born? "))

# Calculate the user's age
current_year = 2023  # You can update this to the current year
user_age = current_year - birth_year

# Determine which standard the user is studying based on age
if user_age <= 5:
    student_standard = "preschool"
elif user_age <= 11:
    student_standard = "elementary school"
elif user_age <= 14:
    student_standard = "middle school"
elif user_age <= 18:
    student_standard = "high school"
else:
    student_standard = "college"

# Print the result
print(f"{user_name}, you are studying in {student_standard}.")

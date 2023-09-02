# Get 5 marks from the student
marks = []
for i in range(5):
    marks.append(int(input("Enter mark {i+1}: ")))

# Calculate the average
average = sum(marks) / len(marks)

# Check eligibility for each college
eligible_colleges = []
if average >= 93:
    eligible_colleges.append("1st College")
if average >= 90:
    eligible_colleges.append("2nd College")
if average >= 89:
    eligible_colleges.append("3rd College")

# Print the eligible colleges
if eligible_colleges:
    print("Student is eligible for admission in {', '.join(eligible_colleges)}.")
else:
    print("Student is not eligible for admission in any college.")
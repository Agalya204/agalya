'''
Get a number from the user. Divide it by 3 and print the result. 
Divide again by 3 and print the result. Keep dividing until the number is less than 3. 
Print the number of times the number was divided
'''
number = float(input("Enter a number: "))
count = 0

while number >= 3:
    number /= 3
    count += 1

print("Number of times divided by 3:", count)

'''

Same as the above. Ask the user if they want only the basic or only the advanced or both.
Print what the user is asking. 
Also ask the user what number table they want to print

'''
# Ask the user for their preference
print("Choose an option:")
print("1. Basic Numbers")
print("2. Advanced Numbers")
print("3. Both Basic and Advanced Numbers")

for i in range (1,6):
    choice = input("Enter your choice (1/2/3): ")
    if choice not in ['1','2','3']:
        print("Invalid choice")
    else:
        break
# Validate the user's choice
# Ask the user for the table number
table_number = int(input("Enter the table number you want to print: "))

# Validate the table number
if table_number < 1 or table_number > 3:
    print("Table number must be between 1 and 3.")
    table_number = int(input("Enter the table number you want to print: "))

# Print the selected table based on the user's preferences
print("\nMy Tables")

if choice == '1':
    print("Table", table_number)
    print("Easy numbers")
    
    # Print basic multiplication table (1 to 10)
    for num in range(1, 11):
        print(f"{table_number} x {num} = {table_number * num}")
    print("*" * 10)

if choice == '2':
    print("Table", table_number)
    print("Advanced numbers")
    
    # Print advanced multiplication table (11 to 20)
    for num in range(11, 21):
        print(f"{table_number} x {num} = {table_number * num}")
    print("*" * 10)

if choice == '3':
    print("Table", table_number)
    print("Easy numbers")
    
    # Print basic multiplication table (1 to 10)
    for i in range(1, 11):
        print(f"{table_number} x {num} = {table_number * num}")
    
    print("Advanced numbers")
    
    # Print advanced multiplication table (11 to 20)
    for num in range(11, 21):
        print(f"{table_number} x {num} = {table_number * num}")
    print("*" * 10)

print("End of tables")

'''
Ask the user which tables he/she wants to print (eg 2,9,7,12)
Also ask if they want to see the basic only or advanced only or both.
Hint - use list to get the user input and learn how to use a list in range statement

'''
# Create a list of all multiplication tables
all_tables = list(range(2, 13))

# Ask the user for input
tables_input = input("Which tables do you want to print (e.g., 2,9,7,12)? ")
option_input = input("Do you want to see basic only, advanced only, or both? ")

# Split the input string into a list of table numbers
tables = [int(table) for table in tables_input.split(',')]

# Convert the option input to lowercase for case-insensitive comparison
option = option_input.lower()

# Print the selected tables based on the user's choice
if option == 'basic':
    for table in tables:
        if 2 <= table <= 5:
            print(f"Table {table}:")
            for i in range(1, 11):
                print(f"{table} x {i} = {table * i}")
elif option == 'advanced':
    for table in tables:
        if 6 <= table <= 12:
            print(f"Table {table}:")
            for i in range(1, 11):
                print(f"{table} x {i} = {table * i}")
elif option == 'both':
    for table in tables:
        if 2 <= table <= 12:
            print(f"Table {table}:")
            for i in range(1, 11):
                print(f"{table} x {i} = {table * i}")
else:
    print("Invalid option. Please choose 'basic', 'advanced', or 'both'.")

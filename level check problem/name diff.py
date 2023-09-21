'''
Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
until the length is equal. 
Eg - input - cat, arrow. (legnth is not equal) 
Output - cataa, arrow (length is equal by adding a)

'''
def make_names_equal(name1, name2):
    len_name1 = len(name1)
    len_name2 = len(name2)
    
    # Calculate the difference in lengths between the two names
    diff = abs(len_name1 - len_name2)
    
    if len_name1 < len_name2:
        # Add 'a' to the end of name1 'diff' times to make lengths equal
        name1 += 'a' * diff
    elif len_name1 > len_name2:
        # Add 'a' to the end of name2 'diff' times to make lengths equal
        name2 += 'a' * diff
    
    return name1, name2

# Get two names from the user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Make the names equal in length
name1, name2 = make_names_equal(name1, name2)

# Print the output
print("Equal length names:", name1, name2)

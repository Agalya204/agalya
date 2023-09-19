'''
    Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.

'''
# Get user input for the password
password = input("Enter a password: ")

# Check if the password is at least 8 characters long
if len(password) < 8:
    print("Weak - Password is too short (must be at least 8 characters long)")
else:
    # Count the number of alphabets, numbers, and special characters
    num_alpha = sum(1 for char in password if char.isalpha())
    num_digits = sum(1 for char in password if char.isdigit())
    num_special = sum(1 for char in password if not char.isalnum())

    # Check if the password contains only alphabets, only numbers, or only special characters
    if num_alpha == 0 or num_digits == 0 or num_special == 0:
        print("Weak - Password consists of only alphabets, numbers, or special characters")
    else:
        # Check if the password meets the criteria for strong or very strong
        if num_alpha >= 3 and num_digits >= 2 and num_special >= 1:
            if len(password) >= 16:
                print("Very strong - Password meets all criteria")
            else:
                print("Strong - Password meets all criteria except length (must be at least 16 characters)")
        else:
            # If none of the above conditions are met, the password is OK
            print("Ok - Password meets the minimum criteria (at least one alphabet, one number, and one special character)")

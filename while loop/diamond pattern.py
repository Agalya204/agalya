'''
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines
'''
# Get the number of lines for the diamond from the user
lines = int(input("Enter number of lines: "))

number = 1

while number <= lines:
    space_input = input("Press the spacebar to print $ ")

    if space_input == " ":
        # Print leading spaces (indentation) and the $ symbols
        print(' ' * (lines - number), end='')
        print('$ ' * number)
        number += 1
    else:
        # If the user presses any key other than space, terminate the program
        print("Exiting the program.")
        break

number -= 2  # Adjust the number to start the lower part of the diamond

while number >= 1:
    space_input = input("Press the spacebar to print $ ")

    if space_input == " ":
        # Print leading spaces (indentation) and the $ symbols
        print(' ' * (lines - number), end='')
        print('$ ' * number)
        number -= 1
    else:
        # If the user presses any key other than space, terminate the program
        print("Exiting the program.")
        break

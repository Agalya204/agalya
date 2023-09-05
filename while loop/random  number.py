'''# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
'''
import random  # Import the random module to generate random numbers

# Generate a random number for the computer to guess between 1 and 10 (adjust the range as needed)
computerNo = random.randint(1, 10)

# Initialize a variable to keep track of the number of attempts
attempt = 0

# Start an infinite loop to keep the game running until the user guesses correctly
while True:
    # Ask the user for their guess and convert it to an integer
    userNo = int(input("Guess the number: "))
    
    # Compare the user's guess to the computer's number
    if userNo < computerNo:
        print("Low")  # If the user's guess is lower, print "Low"
    elif userNo > computerNo:
        print("High")  # If the user's guess is higher, print "High"
    else:
        # If the user's guess is correct, print a congratulatory message and break out of the loop
        print(f"Congratulations! You guessed the number {computerNo} correctly.")
        break
    
    # Increment the attempt counter for each guess
    attempt += 1

# Print the number of attempts it took for the user to guess the correct number
print("User guessed the number in", attempt, "attempts")

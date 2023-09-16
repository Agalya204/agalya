'''
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
'''
inputString = input("Enter a string: ")
i = 0 # counter to track the characters
newString = ""
while i < len(inputString):
    newString += inputString[i:i+2] # assign the characters from i to i+1 of inputString
    newString += " " # add a space
    i += 2

# check to add the remaining characters at the end
if i < len(inputString):
    newString += inputString[i:]

print(newString)

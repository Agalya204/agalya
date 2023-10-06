'''
Problem 1
In the input, find the first A and last A, print all the letters between these two A.
'''

def find_and_print_A(astring):
    astring.lower()
    firstA = astring.find("a")
    if(firstA >= 0):
        lastA = astring.rfind("a")
        if(lastA != firstA):
            print(astring[firstA+1:lastA])
        else:
            print("No second a")
    else:
        print("No a")

astring = input("Enter the string:")
find_and_print_A(astring)

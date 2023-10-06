'''
  In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
'''
def lettersABC(astring, alpha):
    astring = astring.lower()
    alpha = alpha.lower()
    first_alpha = astring.find(alpha)
    stringfound = False
    if first_alpha >= 0:
        last_alpha = astring.rfind(alpha)
        if first_alpha != last_alpha:
            print(astring[first_alpha + 1:last_alpha])
            stringfound = True
        else:
            print(f'No second {alpha}')
    else:
        print(f'No {alpha}')

    return stringfound

astring = input("Enter the string: ")

if not (lettersABC(astring, "a") or lettersABC(astring, "b") or lettersABC(astring, "c")):
    print("No A, B, or C found in the input.")






























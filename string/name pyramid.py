'''
Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM
'''

myName = "agalya"
for letter in range(len(myName)) :
    print(myName[:letter + 1])
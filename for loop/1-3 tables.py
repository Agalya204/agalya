'''
3.My Tables
Table  1
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
**********
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
Table  3
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
**********
End of tables
'''

# Loop through each table
for table in range(1,4):
    print(f"Table",table)
    
    # Loop through the numbers from 1 to 5 for each table
    for num in range(1,6):
        print(table,"*",num,"=",table*num)
    
    print("*" * 10)

# Print the end message
print("End of tables")

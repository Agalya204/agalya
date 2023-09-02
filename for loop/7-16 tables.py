'''
#Print multiplication tables from 7 to 16, each number upto 12 rows.
'''
# Define the range of multiplication tables
start_num = 7
end_num = 16

# Define the number of rows for each table
num_rows = 12

# Loop through the numbers from start_num to end_num
for num in range(start_num, end_num + 1):
    print(f"Multiplication Table for {num}:")

    # Loop through the rows
    for row in range(1, num_rows + 1):
        # Calculate the product
        product = num * row

        # Print the multiplication expression and result
        print(f"{num} x {row} = {product}")

    # Print a newline to separate tables
    print()

'''
#Print Chess board (alternate black and white squares)
#print('\u25A0') - will print white Square. 
You can use "B" to print black squares# Define the size of the chessboard (8x8 for a standard chessboard)
'''
board_size = 8

# Use nested loops to print the chessboard
for row in range(board_size):
    for col in range(board_size):
        # Determine whether to print a white square or a black square based on the row and column indices
        if (row + col) % 2 == 0:
            print('\u25A0', end=' ')  # White square
        else:
            print('\u25A1', end=' ')  # Black square
    print()  # Move to the next row

# Output will be an 8x8 chessboard with alternating black and white squares
'''
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ □ ■
'''
 
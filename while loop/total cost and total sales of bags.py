'''
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold
'''
# Initialize variables
redBags, whiteBags = 100, 200
totalSales, totalBagsSold = 0, 0

# Main loop to sell bags
while totalSales < 10000 and totalBagsSold < 10:
    # Display the number of red and white bags available
    print(f"Red Bags: {redBags}, White Bags: {whiteBags}")

    # Ask customer for input
    color = input("Enter the bag color (red/white): ").strip().lower()
    
    # Check if the selected color is valid
    if color != 'red' and color != 'white':
        print("Invalid color. Please choose 'red' or 'white'.")
        continue

    # Ask customer for the quantity of bags to buy
    quantity = int(input(f"Enter the quantity of {color} bags to buy: "))

    # Check if the shop has enough bags of the selected color
    if color == 'red' and quantity > redBags:
        print("Sorry, we don't have enough red bags.")
        continue
    elif color == 'white' and quantity > whiteBags:
        print("Sorry, we don't have enough white bags.")
        continue

    # Calculate the total cost for the bags
    if color == 'red':
        cost = quantity * 1000
        redBags -= quantity
    else:
        cost = quantity * 1500
        whiteBags -= quantity

    # Increment the total sales and number of bags sold
    totalSales += cost
    totalBagsSold += quantity

# Display total sales and total number of bags sold
print(f"Total Sales: Rs {totalSales}")
print(f"Total Bags Sold: {totalBagsSold}")

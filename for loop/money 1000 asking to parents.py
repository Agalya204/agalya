'''
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.
'''
total_money = 0  # Initialize the total money received
ask_count = 0   # Initialize the count of times asked


for i in range(5):  # Ask up to 5 times
    money_given = int(input("How much money did your parents give you? "))
    
    # Check if the given money is greater than Rs 10
    if money_given > 10:
        total_money += money_given
        print(f"Thank you. You now have Rs {total_money}.")
    else:
        print("Money is too small to count.")
        continue  # Skip adding small amounts
    
    ask_count += 1
    
    if total_money >= 1000:
        break  # If you have Rs 1000 or more, no need to ask again

if total_money >= 1000:
    print(f"You have enough money now. It took {ask_count} attempts.")
else:
    print(f"You were unable to reach Rs 1000 after {ask_count} attempts.")

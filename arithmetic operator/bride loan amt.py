# Problem 9: Start with the above. The total cost is split equally by bride and groom.
# Bride has saved Rs 50000. Determine if the bride has to take a loan or not. If loan, how much?

# Constants
BRIDE_SAVED_AMOUNT = 50000

# Calculate the total cost (same as Problem 8)
LUNCH_COST_PER_PERSON = 200
BREAKFAST_COST_PER_PERSON = LUNCH_COST_PER_PERSON / 2
HALL_COST_PER_PERSON = 200
DECORATION_COST_PERCENTAGE = 0.5
PARKING_COST_PERCENTAGE = 0.1

# Decide what should be the input
num_guests = int(input("Enter the number of guests: "))

# Calculate the cost
lunch_cost = LUNCH_COST_PER_PERSON * num_guests
breakfast_cost = BREAKFAST_COST_PER_PERSON * num_guests
hall_cost = HALL_COST_PER_PERSON * num_guests
decoration_cost = DECORATION_COST_PERCENTAGE * hall_cost
parking_cost = PARKING_COST_PERCENTAGE * hall_cost
total_cost = lunch_cost + breakfast_cost + hall_cost + decoration_cost + parking_cost

# Split the total cost equally between bride and groom
bride_share = total_cost / 2
# Determine if the bride needs to take a loan
if bride_share > BRIDE_SAVED_AMOUNT:
    loan_amount = bride_share - BRIDE_SAVED_AMOUNT
    print(f"The bride needs to take a loan of {loan_amount:.2f} Rs.")
else:
    print("The bride doesn't need to take a loan.")

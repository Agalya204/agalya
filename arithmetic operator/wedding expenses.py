# Problem 8: Calculate wedding expenses.

# Constants
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

# Print the result
print(f"Wedding Expenses:\n"
      f"Lunch cost: {lunch_cost:.2f} Rs\n"
      f"Breakfast cost: {breakfast_cost:.2f} Rs\n"
      f"Hall cost: {hall_cost:.2f} Rs\n"
      f"Decoration cost: {decoration_cost:.2f} Rs\n"
      f"Parking cost: {parking_cost:.2f} Rs\n"
      f"Total cost: {total_cost:.2f} Rs")

# Problem Statement: Write a program to find out how many kilograms of onion or tomato we can buy.
# One kg of Onion costs Rs. 20, and Tomato costs Rs. 10.5. Input is the budget.

budget = float(input("Enter your budget: Rs "))
onion_price = 20.0
tomato_price = 10.5

max_onion_kg = budget / onion_price
max_tomato_kg = budget / tomato_price

print(f"With Rs {budget:.2f}, you can buy {max_onion_kg:.2f} kg of Onion or {max_tomato_kg:.2f} kg of Tomato.")

# Problem Statement: Write a program to find out how many kilograms of onion we can buy,
# considering the price of Onion varies based on the city.
# Chennai - Rs 30, Trichy - Rs 27, Madurai - Rs 34. Input is the budget and city.


budget = float(input("Enter your budget: Rs "))
city = input("Enter your city (Chennai/Trichy/Madurai): ").lower()

onion_prices = {"chennai": 30.0, "trichy": 27.0, "madurai": 34.0}

if city in onion_prices:
  onion_price = onion_prices[city]
  max_onion_kg = budget / onion_price
  print(f"With Rs {budget:.2f} in {city.capitalize()}, you can buy {max_onion_kg:.2f} kg of Onion.")
else:
  print("Invalid city entered.")


# Write a code for calculating electricity bill in tamilnadu. 
# Get user input for consumption
consumption = float(input("Enter the consumption in units: "))
# Check for negative input
if consumption < 0:
    print("Invalid input. Consumption cannot be negative.")
else:
    # Initialize variables for total bill and different charge units and unit cost
    total_bill = 0
    charge_units = [100,200,400,500,600,800,1000]
    unit_cost = [0,2.25,4.5,6,8,9,10,11]

    # Calculate bill based on consumption
    if consumption <= charge_units[0]:
        total_bill = 0
    elif consumption <= charge_units[1]:
        # For consumption between 101 and 200
        total_bill = (consumption - charge_units[0]) * unit_cost[1]
    elif consumption <= charge_units[2]:
        # For consumption between 201 and 400
        total_bill = (charge_units[1] - charge_units[0]) * unit_cost[1] + (consumption - charge_units[1]) * unit_cost[2]
    elif consumption <= charge_units[3]:
        # For consumption between 401 and 500
        total_bill = (charge_units[1] - charge_units[0]) * unit_cost[1] + (charge_units[2] - charge_units[1]) * unit_cost[2] + (consumption - charge_units[2]) * unit_cost[3]
    elif consumption <= charge_units[4]:
        # For consumption between 501 and 600
        total_bill = (charge_units[1] - charge_units[0]) * unit_cost[1] + (charge_units[2] - charge_units[1]) * unit_cost[2] + (charge_units[3] - charge_units[2]) * unit_cost[3] + (consumption - charge_units[3]) * unit_cost[4]
    elif consumption <= charge_units[5]:
        # For consumption between 601 and 800
        total_bill = (charge_units[1] - charge_units[0]) * unit_cost[1] + (charge_units[2] - charge_units[1]) * unit_cost[2] + (charge_units[3] - charge_units[2]) * unit_cost[3] + (charge_units[4] - charge_units[3]) * unit_cost[4] + (consumption - charge_units[4]) * unit_cost[5]
    elif consumption <= charge_units[6]:
        # For consumption between 801 and 1000
        total_bill = (charge_units[1] - charge_units[0]) * unit_cost[1] + (charge_units[2] - charge_units[1]) * unit_cost[2] + (charge_units[3] - charge_units[2]) * unit_cost[3] + (charge_units[4] - charge_units[3]) * unit_cost[4] + (charge_units[5] - charge_units[4]) * unit_cost[5] + (consumption - charge_units[5]) * unit_cost[6]
    else:
        # For consumption beyond 1000
        total_bill = (charge_units[1] - charge_units[0]) * unit_cost[1] + (charge_units[2] - charge_units[1]) * unit_cost[2] + (charge_units[3] - charge_units[2]) * unit_cost[3] + (charge_units[4] - charge_units[3]) * unit_cost[4] + (charge_units[5] - charge_units[4]) * unit_cost[5] + (charge_units[6] - charge_units[5]) * unit_cost[6] + (consumption - charge_units[6]) * unit_cost[7]

    # Print the calculated total bill
    print(f"Electricity Bill: ₹{total_bill:.2f}")

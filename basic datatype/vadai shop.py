def calculate_total_cost():
    vadai_cost = 30
    soda_cost = 20
    sandwich_cost = 100

    vadai_quantity = int(input("Enter the quantity of vadai bought: "))
    soda_quantity = int(input("Enter the quantity of soda bought: "))
    sandwich_quantity = int(input("Enter the quantity of sandwich bought: "))

    total_cost = (vadai_cost * vadai_quantity) + (soda_cost * soda_quantity) + (sandwich_cost * sandwich_quantity)

    print("Total cost is Rs.", total_cost)

    amount_paid = int(input("Enter the amount paid by the user: "))
    change_amount = amount_paid - total_cost
    print("Change amount: Rs.", change_amount)

calculate_total_cost()

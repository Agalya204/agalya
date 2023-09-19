'''
products = [coffee, tea, vadai, biscuit, puffs]
supplies = []
'''
expenses = int(input("Enter todays expenses:"))
coffee_quantity = int(input("Enter no of coffee quantities: "))
tea_quantity = int(input("Enter no of tea quantities: "))
vadai_quantity = int(input("Enter no of vadai quantities: "))
coffee_amount = 10
tea_amount = 15
vadai_amount = 6
print("coffee, tea, vadai")
tea_cost= 0
coffee_cost = 0
vadai_cost = 0
while (True):
    choice = int(input("Enter 1.coffee 2.tea 3.vadai"))
    if choice == 1:
      coffee_order = int(input("Enter no of coffee:"))
      coffee_cost = coffee_order * coffee_amount
      coffee_quantity -= coffee_order
    if choice == 2:
      tea_order = int(input("Enter no of tea:"))
      tea_cost = tea_order * tea_amount
      tea_quantity -= tea_order
    if choice == 3:
      vadai_order = int(input("Enter no of vadai:"))
      vadai_cost = vadai_order * vadai_amount
      vadai_quantity -= vadai_order
    total_amount = coffee_cost + tea_cost +vadai_cost
    print(f"hope you spent amount {total_amount}")
    break
def find_max_or_min():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    choice = input("Do you want to find the max or min? (Enter 'max' or 'min'): ")

    if choice == 'max':
        max_num = max(num1, num2, num3)
        print("The maximum number is:", max_num)
    elif choice == 'min':
        min_num = min(num1, num2, num3)
        print("The minimum number is:", min_num)
    else:
        print("Invalid choice. Please enter 'max' or 'min'.")

find_max_or_min()                
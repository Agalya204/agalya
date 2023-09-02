def swap_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Before swapping: num1 =", num1, "and num2 =", num2)

    # Swapping the numbers using a temporary variable
    temp = num1
    num1 = num2
    num2 = temp

    print("After swapping: num1 =", num1, "and num2 =", num2)

swap_numbers()
def min_coins(number):
    # Create a list to store the minimum coins needed for each value up to the given number
    dp = [float('inf')] * (number + 1)
    dp[0] = 0  # Zero coins needed to make 0

    # Loop through all the values up to the given number
    for i in range(1, number + 1):
        # Check each coin value (1, 3, and 5) and update the minimum coins needed
        if i >= 1:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)

    return dp[number]

# Test the function
if __name__ == "__main__":
    num = int(input("Enter the number: "))
    result = min_coins(num)
    print(f"Minimum coins required to make {num}: {result}")

'''
 Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists.
You can limit the quantity to single digit number.
'''
# List of available fruits
fruits = ["apple", "apples", "orange", "oranges", "banana", "bananas", "grape", "grapes", "mango", "mangoes"]

for i in range(3):  # Run the loop 3 times
    customer_input = input("Vendor: What do you want to buy? ").strip().lower()

    requests = customer_input.split(",")
    fruits_found = []

    for request in requests:
        quantity = 1
        words = request.split()

        for word in words:
            if word.isdigit() and len(word) == 1:
                quantity = int(word)
            elif word in fruits:
                fruit_name = word if word.endswith("s") else word + "s"  # Handle plural forms
                fruits_found.append(f"{quantity} {fruit_name}")

    if fruits_found:
        print(f"Customer: I want {', and '.join(fruits_found)}")
        break  # Exit the loop if a valid request is made
    else:
        print("Customer: I'm sorry, I couldn't understand your request. Please specify a fruit and quantity.")

print("Vendor: Thank you for shopping!")

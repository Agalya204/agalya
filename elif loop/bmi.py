def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Example values (you can replace these with actual values)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
category = categorize_bmi(bmi_result)

print(f"Your BMI is: {bmi_result:.2f}")
print(f"You are categorized as: {category}")

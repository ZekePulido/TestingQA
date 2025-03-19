def calculate_bmi(weight, height):
    weight_kg = weight * 0.45
    
    feet = int(height)
    inches = (height - feet) * 10
    total_inches = feet * 12 + int(inches)
    
    height_m = total_inches * 0.0254
    
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal Weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return round(bmi, 1), category

def main():
    print("Welcome to the BMI Calculator!")
    
    weight = float(input("Please enter your weight (in pounds): "))
    height = float(input("Please enter your height (in feet and inches, e.g., 5.5 for 5 feet 6 inches): "))
    
    bmi, category = calculate_bmi(weight, height)
    
    print(f"\nYour BMI is: {bmi}")
    print(f"Your BMI category is: {category}")

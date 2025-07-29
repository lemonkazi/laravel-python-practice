# # Define a function greet_user(name) that prints a greeting.
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python!")

# # Define calculate_bmi(weight_kg, height_m) and return BMI.
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


# # Define grade_score(score):

# # 90+ → A

# # 80+ → B

# # 70+ → C

# # else → F

def grade_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

def main():
    name = input("Enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    score = int(input("Enter your score: "))

    greet_user(name)
    bmi = calculate_bmi(weight, height)
    grade = grade_score(score)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your grade is: {grade}")

# Call the main function
if __name__ == "__main__":
    main()
# This ensures the main function runs when the script is executed directly.
# If the script is imported as a module, main() won't run automatically.


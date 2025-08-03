def calculate():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()

        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            if second_number == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = first_number / second_number
        else:
            raise ValueError("Unknown operation. Please use +, -, *, or /.")

        print(f"The result of {first_number} {operation} {second_number} is: {result}")

    except ValueError as e:
        print(f"Error: Invalid input. {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Initial calculation
calculate()

# Loop for repeated calculations
while True:
    try_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if try_again == 'yes':
        calculate()
    elif try_again == 'no':
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
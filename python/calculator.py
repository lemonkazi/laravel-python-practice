first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# please ensure the operation is valid
if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
print(f"The result of {first_number} {operation} {second_number} is: {result}")

# without close can i try again take input
try_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
while try_again == 'yes':
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = first_number + second_number
    elif operation == '-':
        result = first_number - second_number
    elif operation == '*':
        result = first_number * second_number
    elif operation == '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Error: Invalid operation."

    print(f"The result of {first_number} {operation} {second_number} is: {result}")
    try_again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
print("Thank you for using the calculator!")
# calculator.py

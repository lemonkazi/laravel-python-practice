# Import functions from all modules from utilities package
from utilities.math_ops import add, multiply, subtract, divide
from utilities.string_ops import capitalize_all
# Call and test each function with sample inputs
def main():
    # Test math operations
    print("Addition of 5 and 3:", add(5, 3))
    print("Multiplication of 4 and 2:", multiply(4, 2))
    print("Subtraction of 10 and 6:", subtract(10, 6))
    print("Division of 8 by 2:", divide(8, 2))
    print("Division by zero test:", divide(8, 0))

    # Test string operations
    words = ["hello", "world", "python"]
    print("Capitalized words:", capitalize_all(words))
if __name__ == "__main__":
    main()

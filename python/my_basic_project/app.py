# Import functions from all modules from utilities package
from utilities.math_ops import add, multiply, subtract, divide
from utilities.string_ops import capitalize_all
from utilities.json_ops import fetch_json_data, save_json_to_file

def main():
    name = "Lemon"  # Example name for testing
    url = "https://api.genderize.io?name=" + name
    json_data = fetch_json_data(url)
    if json_data:
        # Parse and display:
        print("\nParse and display:")
        print("\nName:", json_data.get("name"))
        print("Gender:", json_data.get("gender"))  # Adjust based on actual JSON structure
        print("Probability:", json_data.get("probability"))
    # Also call https://api.nationalize.io?name=yourname

    # Combine both results in one dictionary and save to result.json
    nationalize_url = "https://api.nationalize.io?name=" + name
    nationalize_data = fetch_json_data(nationalize_url)
    if nationalize_data:
        combined_data = {
            "genderize": json_data,
            "nationalize": nationalize_data
        }
        save_json_to_file(combined_data, "result.json")

    # Test math operations
    print("Addition of 5 and 3:", add(5, 3))
    print("Multiplication of 4 and 2:", multiply(4, 2))
    print("Subtraction of 10 and 6:", subtract(10, 6))
    print("Division of 8 by 2:", divide(8, 2))
    print("Division by zero test:", divide(8, 0))

    # Test string operations
    words = ["hello", "world", "python"]
    print("Capitalized words:", capitalize_all(words))
if __name__ == "__main__": # pragma: no cover
    main()

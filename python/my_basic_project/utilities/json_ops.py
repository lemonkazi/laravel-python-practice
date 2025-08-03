import requests

# Create a file: json_api.py

# Call this API: https://api.genderize.io?name=yourname

# Parse and display:

# Name

# Gender

# Probability

# Save the result in a file: result.json

# ✅ Bonus:

# Also call https://api.nationalize.io?name=yourname

# Combine both results in one dictionary and save to result.json
def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()       # Only reached if no exception
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
def save_json_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            import json
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

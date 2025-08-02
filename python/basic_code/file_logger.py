# Ask the user:

# Name

# Today’s activity summary (e.g. "Learned about file handling")

# Create a file log.txt

# Append each entry with:

# Name

# Activity

# Date/time (use from datetime import datetime)

from datetime import datetime
def log_activity(name, activity):
    with open("log.txt", "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {name}: {activity}\n")
def main():
    name = input("Enter your name: ")
    activity = input("Enter today's activity summary: ")

    log_activity(name, activity)
    print("Activity logged successfully.")
    choice = input("Do you want to view the log? (yes/no): ")
    if choice.lower() == "yes":
        with open("log.txt", "r") as file:
            print(file.read())
# Run the main functio
if __name__ == "__main__":
    main()

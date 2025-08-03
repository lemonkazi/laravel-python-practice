#Create a tuple named student_info: (name, age, country)
student_info = ("Lemon", 30, "Bangladesh")
#Create a set languages that includes languages they know (no duplicates)
languages = {"python", "javascript", "python"}  # 'python' is duplicated but will be stored once
#Create a dictionary grades with subject names as keys and marks as values
grades = {
    "math": 85,
    "science": 90,
    "english": 75,
    "history": 80
}
# Print the tuple
print(f"Student Info: {student_info}")
# Print the set language in uppercase
print(f"Languages: {', '.join(languages).upper()}")
# Print the dictionary
print(f"Result:")
total = 0
for subject, mark in grades.items():
    total += mark
    if mark >= 60:
        print(f"{subject}: {mark}: Passed")
    else:
        print(f"{subject}: {mark}: Failed")

# Calculate and print the average mark
average = total / len(grades)
print(f"Average Mark: {average:.2f}")  # formatted to 2 decimal places
#Highest and lowest score
highest_score = max(grades.values())
lowest_score = min(grades.values())
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")


# numbers = [80, 90, 75, 60, 40]


# #Print "Passed" for scores >= 60 and "Failed" for scores < 60
# for score in numbers:
#     if score >= 60:
#         print(f"Score {score}: Passed")
#     else:
#         print(f"Score {score}: Failed")

#Tuples ("Lemon", 30, "Bangladesh")
#set {"python", "javascript", "python"}
# # dictionaries
# user = {
#     "name": "Lemon",
#     "age": 30,
#     "country": "Bangladesh"
# }



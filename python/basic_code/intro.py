first_name = "Lemon"
last_name = "Kazi"
full_name = first_name + " " + last_name
age = input("Enter your age: ") # input will be a string
is_developer = True
height = 5.9
country = "Bangladesh"

# Using f-strings to print the desired output
print(f"My name is {full_name.upper()}")
print(f"I am {age} years old")
print(f"I live in {country.lower()}")
print("I am a developer") # This is printed as a static question
print(f"My height is {height} meters")

print(f"First letter of my name: {first_name[0]}")
print(f"Last letter of my name: {first_name[-1]}")
print(f"replace name: {full_name.replace('Lemon', 'Mamun')}")


# Create a list: [80, 45, 67, 90, 55, 100, 30]

# Use list comprehension to:

# Get all marks >= 60

# Convert all marks to grades (A/B/C/F)

# Create a dictionary with student names as keys and grades as values:

# python
# Copy
# Edit
# names = ["Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "Grace"]

marks = [80, 45, 67, 90, 55, 100, 30]
# Get all marks >= 60
passing_marks = [mark for mark in marks if mark >= 60]
print("Passing Marks:", passing_marks)
# Convert all marks to grades (A/B/C/F)
grades = ['A' if mark >= 90 else 'B' if mark >= 80 else 'C' if mark >= 60 else 'F' for mark in marks]
print("Grades:", grades)
# Create a dictionary with student names as keys and grades as values
names = ["Alice", "Bob", "Charlie", "Diana", "Eva", "Frank", "Grace", "Hannah"]
student_grades = {name: grade for name, grade in zip(names, grades)}
print("Student Grades:", student_grades)
# Output:

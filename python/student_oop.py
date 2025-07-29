class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        else:
            return "F"
    def __str__(self):
        return f"Name: {self.name}, ID: {self.student_id}, Average: {self.average():.2f}, Grade: {self.grade()}"
# Create a student object
student = Student("John Doe", "12345", [85, 90, 78, 92, 88])
# Print student details
print(student)
# Output: Name: John Doe, ID: 12345, Average: 86.60, Grade: B

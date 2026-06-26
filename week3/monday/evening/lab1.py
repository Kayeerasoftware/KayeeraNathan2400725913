class Student:
    def __init__(self, name, age, student_number):
        self.name = name
        self.age = age
        self.student_number = student_number

student1 = Student("Nathan", 25, "24002345")
print(student1.name)
print(student1.age)
print(student1.student_number)
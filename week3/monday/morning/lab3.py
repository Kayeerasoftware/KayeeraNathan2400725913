class Student:
    name="Kayeera"
    nationality="Ugandan"

    def __init__(self, age, religion):
        self.age=age
        self.religion =religion

student1 = Student(25, "protestant")


print(student1.age)
print(student1.religion)
class Persoon:
    def __init__(self, name):
        self.name = name


class Student(Persoon):
    def __init__(self, name, student_number):
        super().__init__(name)
        self.student_number = student_number

        
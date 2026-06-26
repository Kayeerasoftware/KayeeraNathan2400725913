class Person:

    def introduce(self):
        print("I am just a normal human trying to survive life.")


class Man(Person):

    def advice(self):
        print("Real men don't fear exams... they fear the results.")


class Woman(Person):

    def advice(self):
        print("A good hairstyle can increase your confidence before a test.")


class Father(Man):

    def speech(self):
        print("real men face the hardest courses at the university ")


class Mother(Woman):

    def speech(self):
        print("I was more beautiful than you but I managed to study engineering.")


class Children(Father, Mother):

    def homework(self):
        print("Homework is due tomorrow, so today is the perfect day to panic.")


class Boy(Children):

    def exam(self):
        print("I entered the exam room with confidence... and left with new questions.")


class Girl(Children):

    def exam(self):
        print("I revised for six hours, and and gained nothing.")


boy = Boy()
print("\nBoy.mro():")
for cls in Boy.mro():
    print(cls.__name__)
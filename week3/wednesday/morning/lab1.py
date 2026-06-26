class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Dog barks")

dog = Dog()
dog.make_sound()
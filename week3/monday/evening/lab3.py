class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price

    def display_details(self):
        print(f"Price: UGX{self.__price}")


car1 = Car("Toyota", "TX", 2500000)

print("Brand:", car1.brand)      # Public
print("Model:", car1._model)     # Protected

car1.display_details()           # Private
class UnderAgeError(Exception):
    pass


def check_driver_age(age):

    if age < 18:
        raise UnderAgeError(
            "You must be at least 18 years old to drive a car in Uganda."
        )
    print("Congratulations! You are eligible to drive a car.")

try:
    age = int(input("Enter your age: "))

    check_driver_age(age)

except UnderAgeError as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid age.")
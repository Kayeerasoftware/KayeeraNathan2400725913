def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


def get_number(message):

    while True:

        value = input(message).strip()

        if value == "":
            print("Input cannot be empty!")
            continue

        try:
            return float(value)

        except ValueError:
            print("Invalid input! Please enter a valid number.")


while True:

    print("\n" + "=" * 50)
    print("         SMART CALCULATOR SYSTEM")
    print("=" * 50)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    print("-" * 50)

    choice = input("Select Option: ").strip()

    if choice == "5":
        print("\nThank you for using Smart Calculator.")
        print("Program Closed Successfully.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("\nInvalid menu option!")
        continue

    num1 = get_number("Enter First Number : ")
    num2 = get_number("Enter Second Number: ")

    if choice == "1":
        operation = "Addition"
        result = add(num1, num2)

    elif choice == "2":
        operation = "Subtraction"
        result = subtract(num1, num2)

    elif choice == "3":
        operation = "Multiplication"
        result = multiply(num1, num2)

    elif choice == "4":
        operation = "Division"
        result = divide(num1, num2)

    print("\n" + "-" * 50)
    print("             RESULT SUMMARY")
    print("-" * 50)
    print(f"Operation : {operation}")
    print(f"Number 1  : {num1}")
    print(f"Number 2  : {num2}")
    print(f"Result    : {result}")
    print("-" * 50)
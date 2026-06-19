
class InvalidInputError(Exception):
    pass


def log_result(function_name, args, result):

    file = open("log.txt", "a")

    file.write(
        f"{function_name} | Inputs: {args} | Result: {result}\n"
    )

    file.close()



def validate_inputs(func):

    def wrapper(a, b):

        try:

            if not isinstance(a, (int, float)):
                raise InvalidInputError(
                    "First value must be a number"
                )

            if not isinstance(b, (int, float)):
                raise InvalidInputError(
                    "Second value must be a number"
                )

            result = func(a, b)

            log_result(func.__name__, (a, b), result)

            return result

        except InvalidInputError as error:

            return f"Input Error: {error}"

    return wrapper



def safe_divide(func):

    def wrapper(a, b):

        try:
            return func(a, b)

        except ZeroDivisionError:

            log_result(func.__name__, (a, b), "Infinity")

            return "Infinity"

    return wrapper



@validate_inputs
def add(a, b):
    return a + b


@validate_inputs
def subtract(a, b):
    return a - b


@validate_inputs
def multiply(a, b):
    return a * b


@validate_inputs
@safe_divide
def divide(a, b):
    return a / b



def get_number(message):

    while True:

        value = input(message)

        try:
            return float(value)

        except ValueError:
            print("Invalid input. Please enter a number.")



while True:

    print("\n" + "=" * 50)
    print("          ERROR-PROOF CALCULATOR")
    print("=" * 50)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    print("-" * 50)

    choice = input("Select Option: ")

    if choice == "5":
        print("Program Closed Successfully.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid Menu Option")
        continue

    num1 = get_number("Enter First Number : ")
    num2 = get_number("Enter Second Number: ")

    if choice == "1":
        result = add(num1, num2)
        operation = "Addition"

    elif choice == "2":
        result = subtract(num1, num2)
        operation = "Subtraction"

    elif choice == "3":
        result = multiply(num1, num2)
        operation = "Multiplication"

    else:
        result = divide(num1, num2)
        operation = "Division"

    print("\n" + "-" * 50)
    print("              RESULT SUMMARY")
    print("-" * 50)
    print(f"Operation : {operation}")
    print(f"Number 1  : {num1}")
    print(f"Number 2  : {num2}")
    print(f"Result    : {result}")
    print("-" * 50)
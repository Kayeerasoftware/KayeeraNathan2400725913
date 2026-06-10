day_number = int(input("Enter the day of the week as a number (1-7): "))

match day_number:
    case 1:
        day = "Monday"
    case 2:
        day = "Tuesday"
    case 3:
        day = "Wednesday"
    case 4:
        day = "Thursday"
    case 5:
        day = "Friday"
    case 6:
        day = "Saturday"
    case 7:
        day = "Sunday"
    case _:
        day = "Invalid day number"

print("The Day selected is:", day)
def calculate_area(radius):
    area = 3.142 * radius * radius
    return area

radius = float(input("Enter the radius of the circle: "))

result = calculate_area(radius)

print("Area of the circle =", result)




college = "COSIS"

def student():
    name = "Nathan Kayeera"

    print("Inside this function:")
    print("Name:", name)
    print("College:", college)

student()

print("\nOutside the function:")
print("College:", college)
students = list(("Kayeera", "Mukisa", "Brian", "Sarah"))

print("First student:", students[0])
print("Last student:", students[-1])

print("\nAll students:")
for student in students:
    print(student)

students.remove("Mukisa")
print(student)


removed_student = students.pop(1)
print(student)
print("Removed student:", removed_student)
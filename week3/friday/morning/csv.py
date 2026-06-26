import csv

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)



with open("students.csv", "w", newline="") as file:

    fieldnames = ["Name", "Student Number"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({
        "Name": "Kayeera Nathan",
        "Student Number": "A24DEMO20"
    })

print("Student record created successfully.")
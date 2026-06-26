import json
#Writing a json file
# student{
#     name = 
# }
# with open("student.json", "w") as file:
#     json.damp(student,fle, indent=4)


# with open ("students.json", "r") as file:

#     student = json.load(file)
# print(student)


# import json

student = {
    "name": "Kayeera Nathan",
    "student_number": "A24DEMO20",
    "course": "Data Science",
    "age": 24
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")
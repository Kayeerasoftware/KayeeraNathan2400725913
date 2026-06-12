student = dict(
    name="Kayeera",
    age=28,
    student_id=2400725913,
    faculty="Computing",
    results=dict(
        Python=90,
        Java=85,
        Networking=88
    )
)

for key, value in student.items():
    print(key, ":", value)

# for subject, mark in student["results"].items():
#     print(subject, ":", mark)




# for key, value in student.items():

#     if key == "results":

#         print("Results")

#         for subject, mark in value.items():
#             print(subject, ":", mark)

#     else:
#         print(key, ":", value)
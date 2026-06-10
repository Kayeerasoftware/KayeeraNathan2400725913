users = ["admin", "kayeera", "Mukisa"]

username = input("Enter username: ")
password = input("Enter password: ")
message = ""

if username in users:

    if password == "password123":
        message = "Login successful."

    else:
        message = "Password incorrect."

else:
    message = "Username not found."

print(message)
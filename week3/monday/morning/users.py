class User:

    def __init__(self, first_name, last_name, age, email, country):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.email = email
        self.country = country.title()

    def greet_user(self):
        print(f"Hello {self.first_name}! Welcome back.\n")

    def describe_user(self):
        print("\n" + "=" * 50)
        print("                USER PROFILE")
        print("-" * 50)

        self.greet_user()

        print(f"{'Full Name':<15}: {self.first_name} {self.last_name}")
        print(f"{'Age':<15}: {self.age}")
        print(f"{'Email':<15}: {self.email}")
        print(f"{'Country':<15}: {self.country}")

        print("_" * 50)
        print()


# Creating user objects
user1 = User(
    "Nathan",
    "Kayeera",
    25,
    "nathan@gmail.com",
    "Uganda"
)

user2 = User(
    "Sarah",
    "Nantongo",
    22,
    "sarah@gmail.com",
    "Kenya"
)

user3 = User(
    "John",
    "Ssenfuma",
    30,
    "john@gmail.com",
    "Rwanda"
)

# Display user profiles
user1.describe_user()
user2.describe_user()
user3.describe_user()
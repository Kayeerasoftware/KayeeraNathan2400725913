# Kayeera Profile Program

print("-" * 40)
print("      KAYEERA PROFILE SYSTEM")
print("=" * 40)

name = "Kayeera Nathan"
country = "Uganda"
profession = "Software Developer"

print(f"Name       : {name}")
print(f"Country    : {country}")
print(f"Profession : {profession}")

birth_year = int(input("\nEnter your birth year: "))
current_year = 2026

age = current_year - birth_year

print("\n--- Profile Summary ---")
print(f"Hello, {name}!")
print(f"You are approximately {age} years old.")
print(f"You are from {country}.")
print(f"You are pursuing a career as a {profession}.")
print("\nThank you for using the Kayeera Profile System!")
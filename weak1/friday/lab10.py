country = input("Enter the country you want to visit: ")
passport = input("Do you have a valid passport? (yes/no): ")
visa = input("Do you have a valid visa? (yes/no): ")
money = float(input("How much money do you have for accommodation (USD)? "))

if passport.lower() == "yes" and visa.lower() == "yes" and money >= 1000:
    print(f"Congratulations! You are allowed to board the plane to {country}.")

elif passport.lower() != "yes":
    print("You cannot board the plane because you do not have a valid passport.")

elif visa.lower() != "yes":
    print("You cannot board the plane because you do not have a valid visa.")

else:
    print("You cannot board the plane because you need at least $1000 for accommodation.")
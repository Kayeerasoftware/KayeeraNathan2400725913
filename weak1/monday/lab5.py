secret_number = int(input("Enter the secret number: "))

print("\nGuess the secret number!")
attempts = 3

for i in range(1, attempts + 1):
    guess = int(input(f"Attempt {i}/3: Enter your guess: "))

    if guess == secret_number:
        print("\n====================")
        print("   CORRECT NUMBER   ")
        print("====================")
        print(f"You guessed {guess} correctly!")
        break
    else:
        print("Wrong guess!")

if guess != secret_number:
    print("\n====================")
    print("  GAME OVER!")
    print("====================")
    print(f"The correct number was {secret_number}") 
import random

def guess_the_number():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Computer selects a random number
    secret_number = random.randint(1, 100)

    attempts = 0  # Track how many guesses the user makes

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if user_guess < secret_number:
                print("🔼 Too low! Try again.")
            elif user_guess > secret_number:
                print("🔽 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} tries!")
                break

        except ValueError:
            print("⚠️ Please enter a valid integer.")

# Run the game
guess_the_number()

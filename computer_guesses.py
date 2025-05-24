import random

def computer_guesses():
    print("🧠 Think of a number between 1 and 100 and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one possible number

        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == "c":
            print(f"🎉 Yay! I guessed your number in {attempts} attempts!")
            break
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("⚠️ Please enter H, L, or C only.")

# Run the game
computer_guesses()

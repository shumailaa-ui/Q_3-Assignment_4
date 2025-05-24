import random

def play():
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won! 🎉"

    return "You lost. 😢"

def is_win(player, opponent):
    # Return True if player beats opponent
    return (
        (player == "rock" and opponent == "scissors") or
        (player == "scissors" and opponent == "paper") or
        (player == "paper" and opponent == "rock")
    )

# Run the game in a loop
while True:
    result = play()
    print(result)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break

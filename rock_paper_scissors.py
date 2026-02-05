import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock, Paper, Scissors!")
print("Instructions: Type rock, paper, or scissors\n")

while True:
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please try again.\n")
        continue

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win! 🎉")
        user_score += 1

    else:
        print("Result: You lose 😢")
        computer_score += 1

    print(f"\nScore → You: {user_score} | Computer: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing! 👋")
        break

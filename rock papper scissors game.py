import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    """Display the user's choice, computer's choice, and the result."""
    print(f"Your choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    print(result)

def play_game():
    """Play a round of the Rock-Paper-Scissors game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        result = play_game()

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

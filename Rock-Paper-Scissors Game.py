#Rock-Paper-Scissors Game

import random

def get_computer_choice():
    # Randomly choose between rock, paper, or scissors for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    # Compare user and computer choices to determine the winner
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_round():
    # Get user's choice and validate input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return None, None  # Invalid input

    # Get the computer's random choice
    computer_choice = get_computer_choice()

    # Determine the winner
    winner = determine_winner(user_choice, computer_choice)

    # Display the choices and the result
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

    return winner, user_choice

def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        print("\n--- Rock-Paper-Scissors Game ---")

        # Play a round of the game
        winner, user_choice = play_round()
        if winner is None:
            continue  # Invalid input, ask again

        rounds_played += 1

        # Update scores based on the winner
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display current scores
        print(f"\nScore: You {user_score} - Computer {computer_score} (Rounds played: {rounds_played})")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
play_game()

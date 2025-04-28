import random

# Start the game
print("\n-----------------Welcome to Rock-Paper-Scissors Game!----------------")
# Set scores to zero
user_score = 0
computer_score = 0
# Loop for the game
while True:
    # Asking user for input
    print("Choose rock, paper, or scissors:")
    user_choice = input()

    # If user input is not valid, ask again
    if user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors':
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Printing both choices
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determining the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
        user_score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
        user_score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    # Printing the current score
    print(f"Your score: {user_score} | Computer's score: {computer_score}")

    # Ask if the user wants to play again
    print("\nDo you want to play again? (yes or no)")
    play_again = input()
    if play_again.lower() != 'yes':
        print("-------------Thanks for playing!------------")
        break

import random

def get_user_choice():
    print("\nWelcome to the rock paper, scissors game.")
    user_choice = input("Choose rock, paper, or scissors: ")
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    choices = ['rock', 'papaer', 'scissors']
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
  
    play_again = input("Would you like to play again? (yes/no): ")
    if play_again != "yes":
        print("Thank you for playing.")

play_game()

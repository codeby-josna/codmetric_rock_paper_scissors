import random

choice_list = ['rock', 'paper', 'scissors']

def get_computer_move():
    return random.choice(choice_list)

def get_user_move():
    while True:
        user_move = input("Enter your move: ").lower().strip()
        if user_move in choice_list:
            return user_move
        else:
            print("Enter a valid input")

def find_winner(user, computer):
    if user == computer:
        print("RESULT: It's a tie.")
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print("RESULT: You win!")
    else:
        print("RESULT: The computer wins.")

def play_game():
    print("Welcome to Rock-Paper-Scissors Game!!")
    while True:
        player_move = get_user_move()
        computer_move = get_computer_move()
            
        print(f"Computer's move: {computer_move}")
        find_winner(player_move, computer_move)

        retry = input("Play again? (yes/no): ").lower().strip()
        if retry != 'yes':
            print("Thank you for playing!!")
            break

if __name__ == "__main__":
    play_game()
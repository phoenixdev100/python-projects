import random

def print_game_rules():
    print("WELCOME TO SPS (STONE PAPER SCISSORS GAME)\n")
    print("_______!! GAME RULES !!_______")
    print("stone = 'st', paper = 'pa', scissor = 'sc'")
    print("YOUR MAIN GOAL IS TO SCORE 3 POINTS\n")
    print("_______________________________\n")

def get_computer_choice():
    return random.randint(0, 2)

def get_user_choice():
    while True:
        user_input = input("Your choice (st/pa/sc): ").strip().lower()
        if user_input in dict_user:
            return dict_user[user_input]
        else:
            print("Invalid input. Please enter 'st' for stone, 'pa' for paper, or 'sc' for scissor.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'stone' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def print_scores(user_score, computer_score):
    print(f"Your scores are USER: {user_score} COMPUTER: {computer_score}\n")

# Game configuration
dict_comp = {0: 'stone', 1: 'paper', 2: 'scissor'}
dict_user = {'st': 'stone', 'pa': 'paper', 'sc': 'scissor'}

def main():
    print_game_rules()
    
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        comp_choice = get_computer_choice()
        user_choice = get_user_choice()
        
        print(f"YOU CHOSE {user_choice}")
        print(f"COMPUTER CHOSE {dict_comp[comp_choice]}")
        
        winner = determine_winner(user_choice, dict_comp[comp_choice])
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("User wins this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
        print_scores(user_score, computer_score)
    
    if user_score == 3:
        print("___________GAME OVER___________")
        print("USER SMASHED CONQUERED THE GAME")
    else:
        print("___________GAME OVER___________")
        print("COMPUTER CONQUERED THE GAME")

if __name__ == "__main__":
    main()
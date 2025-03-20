# Python game - Rock Paper Sissors
import random

def get_choises():
    player_choice = input( "Enter a choice (rock, paper, sissors: )")
    options = ["rock", "paper", "sissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
    
def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}") 
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "sissors":
            return "Rock smashes sissors! You win!"
        else:
            return "paper covers rock! you lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Sissors cut paper! you lose."
    elif player == "sissors":
        if computer == "paper":
            return "sissors cut paper! You win!"
        else:
            return "rock smashes sissors! you lose."
        
choices = get_choises()
result = check_win(choices["player"], choices["computer"])
print(result)

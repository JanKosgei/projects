#Type in your code here

# Human Vs Computer - Rocks, Papers, Scissors Game

import random

#choice of the computer (using lists)
computer_choices = ["rock", "paper", "scissors"] 
 
#number of rounds 
number_of_rounds = 3 

#Initial scores 
player_score = 0 
computer_score = 0 

#Loop for each round of the game 
for round in range(number_of_rounds): 
	#Prompt the player for their choice 
	player_choice = input("Choose rock, paper, or scissors: ") 
	print(player_choice)
 
# Gameplay scenarios
if player_choice == computer_choices:
        print("It's a tie!")
elif player_choice == 'rock':
        if computer_choices == 'paper':
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
elif player_choice == 'paper':
        if computer_choices == 'scissors':
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
elif player_choice == 'scissors':
        if computer_choices == 'rock':
            print("Computer wins!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
else:
        print("Invalid input. Please try again.")

# Display the  results
print("Game over!,Your score:", player_score, "Computer score:", computer_score)

# To declare the winner
if player_score > computer_score:
    print("You won!")
elif player_score < computer_score:
    print("Computer won!")
else:
    print("It's a tie!")



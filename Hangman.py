#Hangman Game

import random

#creating a list of hangman words 
hangman_words = ["Ford", "Lexus", "Tesla", "Toyota", "Porsche", "Audi", "Mercedes", "Volkswagen", "Jaguar", "Jeep"]

#To check the list
print(hangman_words)

#Selecting a random car
car=random.choice(hangman_words)


# Create an empty list to store the word as dashes
picked = ["_" for x in range(len(car))]

#set the max failed attempts for a player 
max_fails = 6

#wrong guesses 
wrong_guesses = 0

#correct guesses 
correct_guesses = 0

#Playing the game
# Loops 
while wrong_guesses < max_fails and correct_guesses < len(car): 
    letter_guess = input("Guess a letter: ") 
    # check if the letter has already been guessed 
    if letter_guess in picked: 
        print("You have already guessed this letter!") 
    # check if the letter is in the word 
    elif letter_guess in car: 
        # replace the dash with the letter 
        for index, letter in enumerate(car): 
            if letter == letter_guess: 
                picked[index] = letter 
                correct_guesses += 1
        print("".join(picked)) 
    else: 
        print("Wrong guess!") 
        wrong_guesses += 1 
#To end the game 
if wrong_guesses == max_fails: 
    print("You've lost! The word was " + car) 
else: 
    print("You've won!")


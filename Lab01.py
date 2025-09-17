# 1. Name: 
#    Braeden Pope
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    prompts the user for a range of numbers, then generates a random number that 
#    the user has to guess, giving hints on wrong guesses, and then giving the number
#    of guesses as well as what numbers we're guessed upon success.
# 4. What was the hardest part? Be as specific as possible.
#    The hardest part was making sure the variables were the desired way, sometimes they were
#    integers or sometimes strings, but I got it working.
# 5. How long did it take for you to complete the assignment?
#    about an hour and a half hour 

import random
from unittest.mock import sentinel

# Game introduction
print("\n\nThis is the \"guess a number\" game.\n")
# Prompt the user for how difficult the game will be. Ask for an integer
value_max    = int(input("Pick a postive integer: "))
# Generate a random number between 1 and the chosen value
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing
print('You try to guess a number in the smallest amount of attempts.\n\n')
# Initialize the sentinal and the array of guesses
guess        = 0
answer_list  = []
# Play the guessing game
print("Guess a number between 1 and " + str(value_max) + ".")
while guess != value_random:
    # Prompt the user for a number
    guess = int(input("> "))
    # Store the number in an array so it can be displayed later
    answer_list.append(guess)
    # Make a decision: was the guess too high, too low, or just right
    if guess > value_random:
        print('\tToo High!')
    elif guess < value_random:
        print('\tToo Low!')

# Give the user a report: How many guesses and what the guesses where
print('You were able to find the answer in', len(answer_list), 'guesses.')
print('The numbers you guessed were: ', answer_list)

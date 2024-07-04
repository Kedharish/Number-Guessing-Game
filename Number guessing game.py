# BREAKUP OF THE DEV CODE
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. --DONE
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
logo ="""
echo "                                     __                                        __                ";
echo " /| |           /                   /                        /                /                  ";
echo "( | |      _ _ (___  ___  ___      ( __       ___  ___  ___    ___  ___      ( __  ___  _ _  ___ ";
echo "| | )|   )| | )|   )|___)|   )     |   )|   )|___)|___ |___ | |   )|   )     |   )|   )| | )|___)";
echo "| |/ |__/ |  / |__/ |__  |         |__/ |__/ |__   __/  __/ | |  / |__/      |__/ |__/||  / |__  ";
echo "                                                                   __/                           ";
"""
print (logo)
print("Welcome to Number Guessing Game \n")
level_of_difficulty = input("Select one level \n1. Easy \n2. Hard\n").lower()
user_number = int(input("Enter a number from 1 to 100\n"))
chance = 0

# Difficulty level handling

if level_of_difficulty == "1" or level_of_difficulty == "easy":
    chance = 10
elif level_of_difficulty == "2" or level_of_difficulty == "hard":
    chance = 5
else:
    print("Invalid difficulty level selected. Exiting game.")
    exit()

# To validate the user input

def user_input_validation():
    global user_number
    while user_number < 1 or user_number > 100:
        print("Please pick a number from 1 to 100")
        user_number_request = int(input("Enter a number\n"))
        user_number = user_number_request

if user_number < 1 or user_number > 100:
    user_input_validation()

print(f"You picked number: {user_number}")


guess_number = random.randint(1, 100)
print(f"Computer has guessed a number between 1 and 100.")

def range_high():
    global user_number, chance
    while user_number > guess_number and chance > 0:
        print("Too High")
        chance -= 1
        print (f"You only have {chance} Left ! BodySoda Pathuuuu !!!!")
        if chance == 0:
            print(f"You're out of chances. The number was {guess_number}.")
            return
        user_number = int(input("Try again \n"))
    if user_number < guess_number:
        range_low()
    elif user_number == guess_number:
        print("You won! O**A Esala Cup Namde")
        print(f"Computer thought of {guess_number}")

def range_low():
    global user_number, chance
    while user_number < guess_number and chance > 0:
        print("Too Low")
        chance -= 1
        print (f"You only have {chance} Left ! BodySoda Pathuuuu !!!!")
        if chance == 0:
            print(f"You're out of chances. The number was {guess_number}.")
            return
        user_number = int(input("Try again \n"))
    if user_number > guess_number:
        range_high()
    elif user_number == guess_number:
        print("You won! O**A Esala Cup Namde")
        print(f"Computer thought of {guess_number}")

if user_number > guess_number:
    range_high()
elif user_number == guess_number:
    print("You won! W*thA Esala Cup Namde")
    print(f"Computer thought of {guess_number}")
elif user_number < guess_number:
    range_low()

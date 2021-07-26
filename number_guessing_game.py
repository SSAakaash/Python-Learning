# Aakaash SS (26 Jul 2021)
# 
# A simple number guessing game

import random
from os import system, name

# Clears the terminal screen
def clear():
    if name == 'nt':            # For Windows
        _ = system('cls')
    else:                       # For MacOS, Linux
        _ = system('clear')

# Asks you to enter a number, catching the error if you type a non-number
def askNumber(i: int):
    while True:
        try:
            return int(input(f"\nEnter your guess {i}: ").strip())
            break
        except ValueError:
            print("Sorry, please enter a valid number.")

# Asks you whether you want to play again
def playAgain():
    val = input("Do you want to play again? (y/n): ").strip().lower()
    if val == 'y':
        clear()                 # Clears screen if yes
        return True
    else:
        return False

clear()
name = input("\nPlease enter your name: ").strip().lower()
print(f"Hello {name.title()}, Let's play a game!\n")

print("I'm gonna think of a number from 1 to 20, you have 6 tries to guess it.")
print("Ready? Let's begin!")

play_again = True                   # Sets the play state of the game

while play_again:

    number = random.randint(1, 21)  # Generates a random integer from 1-20

    for i in range(1, 7):           # 6 tries

        guess = askNumber(i)

        if guess < number:
            print("The number is higher than your guess")
        elif guess > number:
            print("The number is lower than your guess")
        else:
            print("\nCongrats! You guessed the number!")
            play_again = playAgain()
            break

    if guess != number:
        print(f"\nSorry, the number was {number}")
        play_again = playAgain()
        


print("\nThanks for playing!")





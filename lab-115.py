print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

import random

number = random.randint(1, 10)
isGuessRight = True

while isGuessRight != False:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That correct! You win!".format(guess))
        isGuessRight = False
    else:
        print("You guess {}. That incorrect! You lose!".format(guess))

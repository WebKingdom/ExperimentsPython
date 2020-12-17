import random

TOTAL_GUESSES = 10

numGuesses = 0

name = input("Hi, What is your name? ")

numRange = [0, 10]

number = random.randint(numRange[0], numRange[1])

print("Guess the number between " + str(numRange[0]) + "and" + str(numRange[1]) + name + "! ")

while numGuesses < TOTAL_GUESSES:
    curGuess = int(input('Take guess:'))

    numGuesses += 1

    if curGuess == number:
        print('That is correct!')
        break


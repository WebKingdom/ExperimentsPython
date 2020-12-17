import random

TOTAL_GUESSES = 10


def launch_number_guessing():
    num_guesses = 0

    name = input("Hi, What is your name? ")

    num_range = [0, 10]

    number = random.randint(num_range[0], num_range[1])

    print("Guess the number between " + str(num_range[0]) + " and " + str(num_range[1]) + " " + name + "! ")

    while num_guesses < TOTAL_GUESSES:
        cur_guess = int(input('Take guess: '))

        num_guesses += 1

        if cur_guess == number:
            print('That is correct!')
            break

        if cur_guess < number:
            print('Number is higher.')

        if cur_guess > number:
            print('Number is lower.')

    print('Done!')


launch_number_guessing()

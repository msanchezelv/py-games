import random

number = random.randint(1, 100)

guess  = 0 # User guesses

while guess != number:

    guess = int(input("You have to guess a random number from 1 to a 100, enter your guess: "))

    if (guess < number):
        print("Guess higher!")
    elif (guess > number):
        print("Guess lower!")
    else:
        print("You won!")
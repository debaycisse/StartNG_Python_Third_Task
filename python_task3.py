#!/usr/bin/env python3
import random as rd
# Greet user
print("Hi user, welcome to Number Guessing Game!")


# List the available levels and their definitions
print("""
The available levels are:
Easy : here, you have 6 times attempt to guess a number which is between 1 and 10.
Medium : here, you have 4 times attempt to guess a number which is between 1 and 20.
Hard : here, you have 3 times attempt to guess a number which is between 1 and 50.
""")


# Get user's preferred level
user_preferred_level = input("What level will you like to play?" +
                             "\nType E for (E)asy or M for (M)edium or H for(H)ard ")


# Easy level
if user_preferred_level.lower() == "e" or user_preferred_level.lower() == "easy":
    print("Welcome to Easy Level.")
    random_number = rd.randrange(1, 10)
    guess_attempt = 0
    number_of_allowed_attempt = 6
    while guess_attempt < number_of_allowed_attempt:
        guessed = int(input("Guess: "))
        if guessed == random_number:
            print("You have won!")
            break
        guess_attempt += 1
    else:
        print("You have typed in wrong answer 6 times" +
              "\nYou have failed" +
              "\nGame Over!")



# Medium level
elif user_preferred_level.lower() == "m" or user_preferred_level.lower() == "medium":
    print("Welcome to Medium Level.")
    random_number = rd.randrange(1, 20)
    guess_attempt = 0
    number_of_allowed_attempt = 4
    while guess_attempt < number_of_allowed_attempt:
        guessed = int(input("Guess: "))
        if guessed == random_number:
            print("You have won!")
            break
        guess_attempt += 1
    else:
        print("You have typed in wrong answer 4 times" +
              "\nYou have failed" +
              "\nGame Over!")


# Hard level
elif user_preferred_level.lower() == "h" or user_preferred_level.lower() == "hard":
    print("Welcome to Hard Level.")
    random_number = rd.randrange(1, 50)
    guess_attempt = 0
    number_of_allowed_attempt = 3
    while guess_attempt < number_of_allowed_attempt:
        guessed = int(input("Guess: "))
        if guessed == random_number:
            print("You have won!")
            break
        guess_attempt += 1
    else:
        print("You have typed in wrong answer 3 times" +
              "\nYou have failed" +
              "\nGame Over!")


# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 15:38:24 2022

@author: marco
"""

import random
while True:
    userMax = input("Please give me an upperbound integer: ")
    if (userMax.isnumeric()):
        userMax = int(userMax)
        if (userMax > 1):
            break
        else:
            print("Please enter an integer greater than 1!")
    else:
        print("Please enter positive integers only!")
    
randomNumba = random.randint(1,userMax)

guessCount = 0
userGuess = 0
while userGuess != randomNumba:
    while True:
        userGuess = input("Guess the number: ")
        if (userGuess.isnumeric()):
            userGuess = int(userGuess)
            if (userMax >= userGuess >= 1):
                break
            else:
                print("Please enter a guess within the specified range!")
        else:
            print("Please enter positive integers only!")
    if (userGuess < randomNumba):
        print("Wrong!, try increasing your guess")
        guessCount = guessCount + 1
    else:
        print("Wrong!, try decreasing your guess")
        guessCount = guessCount + 1
print("You got it!")
print("Number of guesses: " + str(guessCount))
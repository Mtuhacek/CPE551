# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:40:41 2022

@author: marco
"""
import random
def main():
    numberGuesser(1,5)

def numberGuesser():
    userMin = input("Please give me a lowerbound integer: ")
    
    userMax = input("Please give me an upperbound integer: ")
    if (userMax.isnumeric()):
        userMin = int(userMin)
        userMax = int(userMax)
        if (userMin % 1 == 0) & (userMax % 1 == 0):
            randomNumba = random.randint(userMin,userMax)
            userGuess = int(input("Guess the number: "))
            guessCount = 1
            while userGuess != randomNumba:
                if (userGuess < randomNumba):
                    print("Wrong!, try increasing your guess")
                    guessCount = guessCount + 1
                    userGuess = int(input("Guess again: "))
                else:
                    print("Wrong!, try decreasing your guess")
                    guessCount = guessCount + 1
                    userGuess = int(input("Guess again: "))
            print("You got it!")
            print("Number of guesses: " + str(guessCount))
                
        else:
            print("Please enter integers only")
    else:
        print("Please enter integers only!")
        
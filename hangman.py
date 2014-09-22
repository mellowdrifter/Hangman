#!/usr/bin/python

import random

class colours:
    def __init__(self):
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.bold = "\033[1m"
        self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.end = "\033[0m"
col = colours()

hangman = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''', '''
 +---+
 |   |
 o   |
     |
     |
     |
=========''', '''
 +---+
 |   |
 o   |
 |   |
     |
     |
=========''', '''
 +---+
 |   |
 o   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 o   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 o   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 o   |
/|\  |
/ \  |
     |
=========''']

def welcome():
    print col.bold+col.yellow+"""
    Welcome to Hangman. These are your options:

    1) Play a new game
    2) Check high scores
    3) Quit
    """+col.end


if __name__ == "__main__":
    welcome()

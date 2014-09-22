#!/usr/bin/python

import random
import os

class colours:
    def __init__(self):
        self.green = "\033[92m"
        self.blue = "\033[94m"
        self.bold = "\033[1m"
        self.yellow = "\033[93m"
        self.red = "\033[91m"
        self.end = "\033[0m"
col = colours()

global guess_number
global guess_letters

guess_number=0
guess_letters=[]

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

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def welcome():
    clearScreen()
    print col.bold+col.yellow+"""
    Welcome to Hangman. These are your options:

    1) Play a new game
    2) Check high scores
    3) Quit
    """+col.end
    gameChoice=raw_input("Please enter your choice: ")
    while gameChoice not in ("1","2","3"):
        return None
    return gameChoice

def playGame():
    global guess_number
    chosen_word="testing"
    len_word=str(len(chosen_word))
    showBoard(None)
    print col.bold+col.yellow+"""
    This word has """+len_word+""" letters in it
    """+col.end
    while guess_number<6:
        letter_choice=choiceLetter()
        if not letter_choice:
            letter_choice=choiceLetter()
        if letter_choice in chosen_word:
            showBoard("c")
        else:
            print "Incorrect!"
            guess_number+=1
            showBoard("i")

def showBoard(x):
    clearScreen()
    if x == "c":
        print col.bold+col.yellow+"    Correct!"+col.end
    elif x == "i":
        print col.bold+col.red+"    Incorrect!"+col.end
    print col.bold+col.yellow+"    This is your current standing:\n\n"+col.red+col.bold+hangman[guess_number]+col.end
    if guess_number<1:
        print col.yellow+col.bold+"\n    No letters have been chosen"+col.end
    elif guess_number<6:
        print col.yellow+col.bold+"\n    These letters have already been incorrectly chosen: "+col.end
    else:
        print col.red+"\nGAME OVER - You lose!"+col.end
        raw_input("\nPress the enter key to go back to the title screen\n")
        titleScreen()

def choiceLetter():
    print "\n"
    choice=raw_input("Choose a letter and press enter: ")
    if not choice.isalpha() or len(choice)>1:
        print "Invalid choice!"
        return None
    else:
        choice=choice.lower()
        return choice

def chooseWord():
#Read words text file and choose a word at random from there. Return the word
    return None

def showScores():
#Read the database and show scores here. Has to be ordered by score. Would be nice to have date as well
    titleScreen()
    return None

def scoreGame():
#Check to see if user can go onto leader list. If top score, make them feel special.
#If user can go onto list, take their name and then display the leaderboard
    return None

def titleScreen():
    global guess_number
    guess_number=0
    guess_letters=[]
    user_choice=welcome()
    while not user_choice:
        user_choice=welcome()
    if user_choice=="1":
        playGame()
    elif user_choice=="2":
        showScores()
    else:
        print "Goodbye!"
        exit()

if __name__ == "__main__":
         titleScreen()



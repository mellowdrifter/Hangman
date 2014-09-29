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

number_of_guesses=0
already_chosen_letters=[]
correct_letters=[]
incorrect_letters=[]
chosen_word="testing"
hidden_word=[]
blanks=""

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
     O   |
         |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========''', '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========''', '''
     +---+
     |   |
     O   |
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
      _____ _____ _____ _____ _____ _____ _____
     |  |  |  _  |   | |   __|     |  _  |   | |
     |     |     | | | |  |  | | | |     | | | |
     |__|__|__|__|_|___|_____|_|_|_|__|__|_|___|

    These are your options:

    1) Play a new game
    2) Check high scores
    3) Quit
    """+col.end
    gameChoice=raw_input("Please enter your choice: ")
    while gameChoice not in ("1","2","3"):
        return None
    return gameChoice

def playGame():
    global number_of_guesses
    global win
    len_word=str(len(chosen_word))
    showBoard(0)
    print col.bold+col.yellow+"""
    This word has """+len_word+""" letters in it
    """+col.end
    while number_of_guesses<6:
        print win
        if win == 1:
            winGame()
        letter_choice=choiceLetter()
        if not letter_choice:
            letter_choice=choiceLetter()
        already_chosen_letters.append(letter_choice)
        if letter_choice in chosen_word:
            correct_letters.append(letter_choice)
            showBoard("c")
        else:
            incorrect_letters.append(letter_choice)
            print "Incorrect!"
            number_of_guesses+=1
            showBoard("i")

def showBoard(x):
    clearScreen()
    print col.bold+col.yellow+"    This is your current standing:\n"+col.red+col.bold+hangman[number_of_guesses]+col.end
    test = showRight()
    if test == 1:
        winGame()
    if x == "c":
        print col.bold+col.yellow+"\n    Correct!"+col.end
    elif x == "i":
        print col.bold+col.red+"\n    Incorrect!"+col.end
    if number_of_guesses<1:
        print col.yellow+col.bold+"\n    No letters have been chosen"+col.end
    elif number_of_guesses<6:
        showWrong()
    else:
        print col.red+"\n\n    GAME OVER - You lose!"+col.end
        raw_input("\nPress the enter key to go back to the title screen\n")
        titleScreen()

def showWrong():
    print col.yellow+col.bold+"\n    These letters have already been incorrectly chosen: "+col.end,
    for i in incorrect_letters:
        print col.yellow+col.bold+i+col.end,

def showRight():
    print col.bold+col.yellow+"\n    Current word: "+col.end,
    blanks="_"*len(chosen_word)
    for i in range(len(chosen_word)):
        if chosen_word[i] in correct_letters:
            blanks=blanks[:i]+chosen_word[i]+blanks[i+1:]
    for letter in blanks:
        print letter,
    return blanks

def winGame():
    clearScreen()
    print "Congratulations, you've got the word!"
    raw_input("Press enter to continue...")
    titleScreen()

def choiceLetter():
    print "\n"
    choice=raw_input("Choose a letter and press enter: ")
    if not choice.isalpha() or len(choice)>1:
        print "Invalid choice!"
        return None
    elif choice.lower() in already_chosen_letters:
        print "You already gave that letter!"
    else:
        already_chosen_letters.append
        return choice.lower()

def chooseWord():
#Read words text file and choose a word at random from there. Return the word
    pass

def showScores():
#Read the database and show scores here. Has to be ordered by score. Would be nice to have date as well
    titleScreen()


def scoreGame():
#Check to see if user can go onto leader list. If top score, make them feel special.
#If user can go onto list, take their name and then display the leaderboard
    pass

def titleScreen():
    global win
    already_chosen_letters=[]
    blanks=""
    user_choice=welcome()
    win = 0
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



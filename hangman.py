# -*- coding: utf-8 -*-
# hangman
# TODO: Add functionality to check if the inputted word is the correct answer!
import random

words = "cat,dog,python,monty,golden egg,raxacoricafallapatorius"
wordslist = words.split(",")

running = True
fails = 0

# A function to print out the board
def printBoard(word):
    empty_word = ""
    for i in range(len(word)):
        if word[i] == " " or word[i] in correct_letters:
            empty_word += word[i]
        else:
            empty_word += "_"
    return empty_word

# The random word, and the lists holding the guessed_letters and the correct_letters
word = random.choice(wordslist)
guessed_letters = []
correct_letters = []

print "{0} is the blank word! Please write your letter below!".format(printBoard(word))

while running:
    output = printBoard(word)

    # Get the first letter
    print output
    letter = raw_input("> ")

    # Check if the input is longer than 1
    if len(letter) > 1:
        letter = letter[0]
        print "{0} is longer than one letter, {1} was chosen as input.".format(letter, letter[0])

    # Check if letter is guessed, or if it is in word.
    if letter in guessed_letters or letter in correct_letters:
        print "You have already guessed this letter!"
    elif letter in ",.-1234567890+¨'^~*!#¤%&/()=@£$€[]_:;|§>< ":
        print "Not valid characters! Try again."
    elif letter in word:
        print "{0} is in word! Woohoo!".format(letter)
        guessed_letters.append(letter)
        correct_letters.append(letter)
    else:
        print "Bummer! {0} was not in the word! {1} tries left!".format(letter, 5-fails)
        guessed_letters.append(letter)
        fails += 1

        # Check if the user have won
    if output == word:
        print "You have won the game!"
        running = False

        # Check if the user have lost
    if fails > 5:
        print "You lost the game!"
        running = False

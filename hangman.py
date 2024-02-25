# BANNER and HANGMAN_PICS are some ASCII art
# Create your own ASCII art if you desire, but
# ONLY AFTER getting the game logic working.
from ascii_art import BANNER, HANGMAN_PICS
import random

# uncomment the import statement, below, when
# you're ready to implement a one player version
# of the game.
# `animal_words` is a list of . . . animal words.
# Feel free to add more words or word categories.
from word_lists import animal_words

"""
Here's where you'll write your code. 
  - Follow the instructions in the README file.
  - If you try to write all the code in `play_hangman`, 
    it's going to be a mess. Instead, break your logic
    into smaller functions that you can call from 
    `play_hangman`.

Run your code from the terminal:
  - make sure you're in the right directory (`projects/hangman`)
    - if you're not sure how to get to the right directory, ask!
  - make sure you're at the command line prompt, not in the Python shell (not >>>)
  - type the following command: python hangman.py

Tests? No tests for this project. 
"""


# Here's where you can define helper functions


# `play_hangman` is the main function, the function
# that will orchestrate all the helper functions
# you define, above.


def hangman(again = False, winstreak = 0):
  if again:
    replay = input("Do you want to play again? (y/n)")
    print("\n" * 15)
    print(f"You won {winstreak} time(s) in a row!")
    if replay == 'n':
      return
  else:
    print(BANNER)
  multiplayer = input("Multiplayer (y/n)")
  word = random.choice(animal_words)
  if not multiplayer == 'n':  
    word = input("Enter the word:")
    
  print('\n' * 20)
  print('_ ' * len(word))
  letter_corrects = []
  letter_wrongs = []
  tries = 5
  guess(word, letter_corrects, letter_wrongs, tries, winstreak)

def guess(word, letter_corrects, letter_wrongs, tries, winstreak):
    letter = input('Guess a letter:')
    blank = []
    if letter in word:
        letter_corrects.append(letter)
        blank = []
        calculate_blanks(blank, word, letter_corrects)
        print_data(tries, blank, letter_corrects, letter_wrongs)
        if '_' not in blank:
            print('You win! :)')
            return hangman(True, winstreak + 1)
        print(f"Correct! {tries} tries left.")
        guess(word, letter_corrects, letter_wrongs, tries, winstreak)
    else:
        calculate_blanks(blank, word, letter_corrects)
        letter_wrongs.append(letter)
        tries -= 1
        print_data(tries, blank, letter_corrects, letter_wrongs)
        if tries == 0:
            print(f"You Lost. :(\nThe word was: {word}!")
            return hangman(True, 0)
        print(f"Wrong letter! {tries} tries left.")
        guess(word, letter_corrects, letter_wrongs, tries, winstreak)
   
def calculate_blanks(blank, word, letter_corrects):
  for eachletter in word:
    blank.append('_')
    for correctletters in letter_corrects:
      if(eachletter == correctletters):
        blank.pop()
        blank.append(eachletter)

def print_data(tries, blank, letter_corrects, letter_wrongs):
    blanks = " ".join(blank)
    wrong_guesses = " ".join(letter_wrongs)
    correct_guesses = " ".join(letter_corrects)

    print(HANGMAN_PICS[tries], 
    "\n", blanks, "\n"
    f"\nCorrect Guesses: {correct_guesses}", 
    f"\nIncorrect Guesses: {wrong_guesses}\n")

"""
Don't worry about the code below, and don't change it.

It's just a way to trigger the `play_hangman` function
when you run this file from the command line.
"""

if __name__ == "__main__":
  hangman()

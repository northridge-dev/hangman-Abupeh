# BANNER and HANGMAN_PICS are some ASCII art
# Create your own ASCII art if you desire, but
# ONLY AFTER getting the game logic working.
from ascii_art import BANNER, HANGMAN_PICS

# uncomment the import statement, below, when
# you're ready to implement a one player version
# of the game.
# `animal_words` is a list of . . . animal words.
# Feel free to add more words or word categories.
# from word_lists import animal_words

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
def hangman(again = False):
  if again:
    replay = input("Do you want to play again? (y/n)")
    if replay == 'n':
      return
  else:
    print(BANNER)
  word = input("Enter the word:")
  print('\n' * 20)
  print('_ ' * len(word))
  letter_list = []
  letter_wrongs = []
  tries = 5
  guess(word, letter_list, letter_wrongs, tries)

def guess(word, letter_list, letter_wrongs, tries):
    letter = input('Guess a letter:')
    blank = []
    if letter in word:
        letter_list.append(letter)
        blank = []
        for eachletter in word:
            blank.append('_')
            for correctletters in letter_list:
                if(eachletter == correctletters):
                    blank.pop()
                    blank.append(eachletter)
        if '_' not in blank:
            print('You win! :)')
            return hangman(True)
        print_data(tries, blank, letter_wrongs)
        print(f"Correct! {tries} tries left.")
        guess(word, letter_list, letter_wrongs, tries)
    else:
        letter_wrongs.append(letter)
        tries -= 1
        if tries == 0:
            print("You Lost. :(")
            return hangman(True)
        print_data(tries, blank, letter_wrongs)
        print(f"Wrong letter! {tries} tries left.")
        guess(word, letter_list, letter_wrongs, tries)
   
def print_data(tries, blank, letter_wrongs):
    correct_letters = " ".join(blank)
    wrong_guesses = " ".join(letter_wrongs)
    print(HANGMAN_PICS[tries], 
    f"\nCorrect Guesses: {correct_letters}", 
    f"\n Incorrect Guesses: {wrong_guesses}")

"""
Don't worry about the code below, and don't change it.

It's just a way to trigger the `play_hangman` function
when you run this file from the command line.
"""
if __name__ == "__main__":
    hangman()

# Author: Jamal Huraibi, fh1328
# Assignment 03
# Question 01

# -------------------------------------------------------------------------------------------------------------------- #

# Instructions Outline:
#   [1] Read input file
#   [2] Pick a word randomly
#   [3] Scramble random word
#   [4] Ask player to guess the word
#   [5] After each round:
#   	- Give user their points if guessed correctly
#   	- Ask if use wants to continue or not
#   	- Start new game (repeat)

# Requirements:
#   Only use breezypythongui widgets for GUI
#   Pick the words randomly and display the scrambled words to the player to guess the original ones:
#  	    - Give the player 3 chances to guess a word, and show the number of guesses left
#  	    - After each round, ask the player if they want to continue the game
#  	    - If the guess is correct print “Congratulation, you won!”
#  	    - If the guess is incorrect, print “Sorry, you didn’t win”, and show the original word.
#   Display the player’s total score after each play
#   Display all the information on the game window (No input/output from or to the console)
#   Provide instant feedback for every interaction
#   Organize your widgets in a coherent design
#   All buttons and controllers must work properly
#   Feel free to make any changes necessary

# -------------------------------------------------------------------------------------------------------------------- #

# PEP8 CURRENTLY NOT BEING FOLLOWED


import random
from breezypythongui import EasyFrame


class GUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Unscramble the Word")
        self.addLabel(text="Try to unscramble the word: ", row=0, column=0)
        self.addLabel(text="Your Guess: ", row=0, column=0)


class Game:
    def __init__(self):
        self.secret_word = None
        self.scrambled_secret_word = None
        self.word_bank = None
        self.__process_words_file()
        self.__shuffle_words()
    
    def __process_words_file(self):
        """Removes commas from text file. Delimits the words by SPACE and saves as List."""
        file_in_stream = open("words.txt", 'r')                                 # Open the in-stream file in read mode
        file_contents = file_in_stream.read()                                   # Store file contents as single string
        file_contents = file_contents.replace(',', '')                          # Remove the commas (',')
        
        self.word_bank = file_contents.split()                                  # Save as list of individual words
    
    def __shuffle_words(self):
        """Randomize the list of words"""
        random.shuffle(self.word_bank)                                          # Randomize the order of the words
    
    def start_game(self):
        """Picks and scrambles the next secret word (if word_bank is not empty)"""
        if self.games_remaining():
            self.__pick_secret_word()
            self.__scramble_word()
            # Show a prompt asking for guesses
        else:
            print("No Games Remaining")
            # Show a prompt asking if user wants to play again or exit
    
    def __pick_secret_word(self):
        """Pops off the next word from the list"""
        self.secret_word = self.word_bank.pop()                                 # Get secret word (and delete from list)
    
    def __scramble_word(self):
        """Scrambles the characters in the secret word"""
        word = list(self.secret_word)                                           # Convert word to List of characters
        
        random.shuffle(word)                                                    # Randomly move around the letters
        word = ''.join(word)                                                    # "Convert" back to a single string
        
        self.scrambled_secret_word = word                                       # Store scrambled version of the word
    
    def games_remaining(self):
        return len(self.word_bank) > 0
        

if __name__ == '__main__':
    game = Game()
    
    game.start_game()
    game.show_scrambled_word()
    game.get_user_guess()
    #game.check_if_guess_correct
    #game.
    #game.get_user_input()
    

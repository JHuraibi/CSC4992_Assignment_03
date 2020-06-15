# Author: Jamal Huraibi, fh1328
# Assignment 03
# Question 01

# PEP8 CURRENTLY NOT BEING FOLLOWED


import random
from breezypythongui import EasyFrame


class ScrambledWordGame(EasyFrame):
    def __init__(self):
        # Separate "initialize" for game variables
        self.initialize_game_variables()
        
        EasyFrame.__init__(self, width=400, height=200, title="Unscramble the Word")
        # Label and field for the Score
        self.addLabel(text="Score: ", column=0, row=0)
        self.fieldScore = self.addIntegerField(value=0, state="readonly", column=1, row=0)
        
        # Label and field for the Scrambled Word
        self.addLabel(text="Scrambled Word: ", column=0, row=1)
        self.fieldScrambled = self.addTextField(text="", state="readonly", column=1, row=1)
        
        # Label and field for the Player's Guess Input
        self.addLabel(text="Your Guess: ", column=0, row=2)
        self.fieldGuess = self.addTextField(text="", column=1, row=2)
        
        # Label and field for number of Guesses Remaining
        self.addLabel(text="Tries Remaining: ", column=0, row=3)
        self.fieldNumTries = self.addIntegerField(value=0, state="readonly", column=1, row=3)
        
        # Button to Submit Guess
        self.addButton(text="Check Guess", column=2, row=4, command=self.process_player_guess)
        
        # Button to Start a New Game
        self.addButton(text="Start New Game", column=1, row=4, command=self.start_new_game)
    
    def initialize_game_variables(self):
        self.word_bank = None
        self.secret_word = None
        self.scrambled_secret_word = None
        self.guess = None
        self.score = 0
        self.previous_guesses = []
        self.process_words_file()
        self.shuffle_words()
        
    def process_words_file(self):
        """Removes commas from text file. Delimits the words by SPACE and saves as List."""
        file_in_stream = open("words.txt", 'r')                                 # Open the in-stream file in read mode
        file_contents = file_in_stream.read()                                   # Store file contents as single string
        file_contents = file_contents.replace(',', '')                          # Remove the commas (',')
    
        self.word_bank = file_contents.split()                                  # Save as list of individual words

    def shuffle_words(self):
        """Randomize the list of words"""
        random.shuffle(self.word_bank)                                          # Randomize the order of the words

    def start_new_game(self):
        """Sets and scrambles the next secret word (if word_bank is not empty)"""
        if self.games_remaining():
            self.set_secret_word()
            self.scramble_word()
        else:
            self.messageBox(title="No Games", message="No Words Remaining!")

    def set_secret_word(self):
        """Pops off the next word from the list"""
        self.secret_word = self.word_bank.pop()                                 # Get secret word (and delete from list)

    def scramble_word(self):
        """Scrambles the characters in the secret word"""
        word = list(self.secret_word)                                           # Convert word to List of characters
    
        random.shuffle(word)                                                    # Randomly shuffle around the letters
        word = ''.join(word)                                                    # "Convert" back to a single string
    
        self.scrambled_secret_word = word                                       # Store scrambled version of the word

    def process_player_guess(self):
        """Gets the player's guess. Alerts if guess non-alpha or already tried.
        Will record the guess if it was valid"""

        guess = self.fieldGuess.getText()                                       # Get player's guess from the text field

        no_guess_entered = len(guess) == 0                                      # No guess entered
        valid_guess = str(guess).isalpha()                                      # Only letters entered?
        old_guess = self.guess_already_tried(guess)                             # Guess already tried?

        if no_guess_entered:
            self.messageBox(title="Invalid Guess",
                            message="No Guess Entered")                         # Nothing was entered
        elif not valid_guess:
            self.messageBox(title="Invalid Guess",
                            message="Guesses can only have letters!")           # Invalid guess entered (non-alpha)
        elif old_guess:
            self.messageBox(title="Invalid Guess",
                            message="\"{}\" was already tried".format(guess))   # Guess was already tried
        else:
            self.record_guess(guess)                                            # Guess was good, record it

    def guess_already_tried(self, guess):
        """Returns true if the player's guess matches a guess they already attempted"""
        return guess.lower() in self.previous_guesses
    
    def record_guess(self, guess):
        """Records the most-recent valid guess by converting to lower case and adding to List"""
        lower_case_guess = guess.lower()
        self.previous_guesses.append(lower_case_guess)

    def guessed_correctly(self, guess):
        """Returns true if the player's guess was correct (matches the secret word)"""
        return str(guess).lower() == self.secret_word.lower()
    
    def games_remaining(self):
        """Returns whether there are any available games left (i.e. there are words in word_bank)"""
        return len(self.word_bank) > 0
    

def main():
    ScrambledWordGame().mainloop()


if __name__ == '__main__':
    main()
    

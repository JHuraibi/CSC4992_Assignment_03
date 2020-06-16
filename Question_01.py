# Author: Jamal Huraibi, fh1328
# Assignment 03
# Question 01

import random
from breezypythongui import EasyFrame


class ScrambledWordGame(EasyFrame):
    def __init__(self):
        self.word_bank = None
        self.secret_word = None
        self.scrambled_secret_word = None
        self.guess = None
        self.score = 0
        self.tries_remaining = 3
        self.previous_guesses = []
        
        EasyFrame.__init__(self, width=400, height=200, title="Unscramble the Word")
        
        # Label and field for the Scrambled Word
        self.addLabel(text="Scrambled Word: ", row=0, column=0)
        self.fieldScrambledWord = self.addTextField(text="", state="readonly", row=0, column=1)

        # Label and field for the Score
        self.addLabel(text="Score: ", sticky="E", row=0, column=3)
        self.fieldScore = self.addIntegerField(value=0, state="readonly", sticky="W", row=0, column=4)
        
        # Label and field the Player's Guess Input
        self.addLabel(text="Your Guess: ", sticky="E", row=1, column=0)
        self.fieldGuess = self.addTextField(text="", row=1, column=1)

        # Label and field number of Guesses Remaining
        self.addLabel(text="Tries Remaining: ", row=2, column=0)
        self.fieldTriesRemaining = self.addIntegerField(value=0, state="readonly", sticky="W", row=2, column=1)
        
        # Bottom-most label for messages to player
        self.labelMessage = self.addTextField(text="", state="readonly", sticky="NSEW",
                                              columnspan=5, row=4, column=0)

        # Buttons
        self.checkGuessButton = self.addButton(text="Check Guess", row=3, column=0, command=self.process_player_guess)
        self.newGameButton = self.addButton(text="New Game", row=3, column=3, command=self.start_new_game)
        
        self.preliminary_work()                                                 # Execute preliminary tasks
    
    def preliminary_work(self):
        """Checks if text file exists and continues if it does. Otherwise, exits program"""
        import os
        text_file_exists = os.path.exists("words.txt")                          # Check for text file of words
        
        if not text_file_exists:
            print("Error opening text file.")
            exit()
            
        self.process_words_file()                                               # Load words from text file
        self.shuffle_words()                                                    # Randomize the list of words
        self.start_new_game()                                                   # Start the game
    
    def process_words_file(self):
        """Removes commas from text file. Delimits the words by SPACE and saves as List."""
        file_in_stream = open("words.txt", 'r')                                 # Open the in-stream file in read mode
        file_contents = file_in_stream.read()                                   # Store file contents as single string
        file_contents = file_contents.replace(',', '')                          # Remove the commas (',')
        
        self.word_bank = file_contents.split()                                  # Save as list of individual words
        file_in_stream.close()                                                  # Close the file stream
        
        return True

    def shuffle_words(self):
        """Randomize the list of words"""
        random.shuffle(self.word_bank)                                          # Randomize the order of the words

    def start_new_game(self):
        """Tasks to be done before a new game starts"""
        self.set_secret_word()                                                  # Set the secret word
        self.scramble_word()                                                    # Scrambles the letters of the word
        self.tries_remaining = 3                                                # Reset tries to 3
        self.previous_guesses = []                                              # Clear previous guesses
        
        self.fieldGuess.setText("")                                             # Clear the guess textbox
        self.fieldScrambledWord.setText(self.scrambled_secret_word)             # Update Scrambled Word
        self.fieldTriesRemaining.setValue(self.tries_remaining)                 # Update (reset) tries remaining
        
        self.checkGuessButton["state"] = "normal"                               # Enable "Check Guess" button
        self.newGameButton["state"] = "normal"                                  # Ensure "New Game" button is enabled
        self.labelMessage.setText("")                                           # Clear the bottom message label
        print("WORD: {}".format(self.secret_word))  # !! FOR TESTING

    def games_remaining(self):
        """Returns whether there are any available games left (i.e. words remaining in List word_bank)"""
        return len(self.word_bank) > 0

    def set_secret_word(self):
        """Pops off the next word from the shuffled List"""
        self.secret_word = self.word_bank.pop()                                 # Get secret word (and delete from list)

    def scramble_word(self):
        """Scrambles the characters in the secret word.
        Loop will handle off-chance scrambled word is still equals the original."""
        word = self.secret_word
        
        while word == self.secret_word:
            word = list(self.secret_word)                                       # Convert word to List of characters
            random.shuffle(word)                                                # Randomly shuffle around the letters
            word = ''.join(word)                                                # "Convert" back to a single string
            
        self.scrambled_secret_word = word                                       # Store scrambled version of the word

    def process_player_guess(self):
        """Extracts the player's guess.
        Alerts if guess non-alpha or already tried.
        Otherwise, continues with following game mechanics"""

        guess = self.fieldGuess.getText()                                       # Get player's guess from the text field
        self.fieldGuess.setText("")                                             # Clear the guess textbox

        no_guess_entered = len(guess) == 0                                      # No guess entered
        valid_guess = str(guess).isalpha()                                      # Only letters entered?
        old_guess = self.guess_already_tried(guess)                             # Guess already tried?

        if no_guess_entered:
            self.labelMessage.setText("No Guess Entered")                       # Nothing was entered
        elif not valid_guess:
            self.labelMessage.setText("Guesses can only have letters!")         # Invalid guess entered (non-alpha)
        elif old_guess:
            self.labelMessage.setText("\"{}\" already tried".format(guess))     # Guess was already tried
        else:
            self.guess = guess                                                  # Guess entered was good, store it
            self.check_guess()                                                  # Check guess
            
    def check_guess(self):
        """Skips program to end-of-game procedures if guess was correct"""
        current_guess = self.guess.lower()                                      # Convert guess string to lowercase
        secret_word = self.secret_word.lower()                                  # Ensure secret word is lowercase
        
        if current_guess == secret_word:
            self.update_score()                                                 # Update their score
            self.messageBox(title="", message="Congratulations, you won!")      # User guessed word correctly
            self.end_game()                                                     # Execute end-game tasks
        else:
            self.next_round()                                                   # Incorrect, execute end-of-round tasks

    def guess_already_tried(self, guess):
        """Returns true if the player's guess matches a guess they already attempted"""
        return guess.lower() in self.previous_guesses

    def record_guess(self, guess):
        """Records the most-recent valid guess by converting to lower case and adding to List"""
        lower_case_guess = guess.lower()
        self.previous_guesses.append(lower_case_guess)
    
    def update_score(self):
        """Updates the player's score and updates the output on the GUI"""
        points_earned = len(self.secret_word) * 10                              # 10 pts. for each letter of secret word
        self.score = self.score + points_earned                                 # Add to total score
        
        self.fieldScore.setValue(self.score)                                    # Update score on GUI

    def next_round(self):
        """Handles end of round actions"""
        self.tries_remaining = self.tries_remaining - 1                         # Deduct a try
        self.fieldGuess.setText("")                                             # Clear the guess textbox
        
        if self.tries_remaining > 0:
            self.previous_guesses.append(self.guess)                            # Record most-recent guess tried
            self.fieldTriesRemaining.setNumber(self.tries_remaining)            # Update tries user has remaining
            self.labelMessage.setText("The guess was incorrect.")               # Inform player guess was wrong
        else:
            self.messageBox(title="", message="Sorry, you didn’t win")          # No tries remaining
            self.end_game()                                                     # Execute end-game tasks

    def end_game(self):
        """Handles end of game tasks"""
        if self.games_remaining():
            self.checkGuessButton["state"] = "disabled"                         # Disable "Check Guess" button
            self.labelMessage.setText("Click \"New Game\" to continue")         # Tell user how to play again
        else:
            self.labelMessage.setText("No Words Remaining!")                    # Inform player no games left
            self.checkGuessButton["state"] = "disabled"                         # Disable the buttons
            self.newGameButton["state"] = "disabled"


def main():
    """Instantiates the GUI window and starts the game"""
    ScrambledWordGame().mainloop()


if __name__ == '__main__':
    main()
    

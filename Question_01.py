# Author: Jamal Huraibi, fh1328
# Assignment 03
# Question 01

# PEP8 CURRENTLY NOT BEING FOLLOWED


import random
from breezypythongui import EasyFrame


class GUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Unscramble the Word")
        self.addLabel(text="Try to unscramble the word: ", row=0, column=0)
        self.addLabel(text="Your Guess: ", row=0, column=0)


class Game(GUI):
    def __init__(self):
        self.secret_word = None
        self.scrambled_secret_word = None
        self.word_bank = None
        self.guess = None
        self.previous_guesses = []
        self.__process_words_file()
        self.__shuffle_words()

    @staticmethod
    def guess_valid(value_entered):
        return str(value_entered).isalpha()
    
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
            # Show a prompt asking if player wants to play again or exit
    
    def __pick_secret_word(self):
        """Pops off the next word from the list"""
        self.secret_word = self.word_bank.pop()                                 # Get secret word (and delete from list)
    
    def __scramble_word(self):
        """Scrambles the characters in the secret word"""
        word = list(self.secret_word)                                           # Convert word to List of characters
        
        random.shuffle(word)                                                    # Randomly shuffle around the letters
        word = ''.join(word)                                                    # "Convert" back to a single string
        
        self.scrambled_secret_word = word                                       # Store scrambled version of the word
    
    def games_remaining(self):
        """Returns whether there are any available games left (i.e. there are words in word_bank)"""
        return len(self.word_bank) > 0

    def get_player_guess(self):
        """Gets the player's guess. If guess non-alpha or already tried, reattempt. Then stores the guess"""
        # If time: Determine if functions below are unnecessary
        self.guess = self.__guess_helper()
        
        
    def __guess_helper(self):
        """Recursive method to get player's guess and check if its valid"""
        guess = input("Enter Your Guess: ")                                     # Get the player's guess
        
        valid_guess = self.__has_letters_only(guess)                            # Only letters entered?
        old_guess = self.__guess_already_tried(guess)                           # Guess already tried?
        
        if not valid_guess:
            print("\nInvalid guess. Letters only!")                             # Invalid guess (non-alpha)
            return self.__guess_helper()
        elif old_guess:
            print("\n\"{}\" was already tried".format(guess))                   # Guess was already tried
            return self.__guess_helper()
        else:
            return guess                                                        # (Base Case): Guess is valid
        
    def __record_guess(self, most_recent_guess):
        self.previous_guesses.append(most_recent_guess)
        
    def __has_letters_only(self, guess):
        """Returns true if the player's guess only contains letters"""
        return str(guess).isalpha()
    
    def __guess_already_tried(self, guess):
        """Returns true if the player's guess matches a guess they already attempted"""
        return guess in self.previous_guesses
        
    def guessed_correctly(self, guess):
        """Returns true if the player's guess was correct (matches the secret word)"""
        return str(self.guess) == self.secret_word


if __name__ == '__main__':
    game = Game()

    game.start_game()
    
    print("Word: {}".format(game.secret_word))
    game.get_player_guess()
    if game.guessed_correctly():
        print("You Win!")
    
    # game.play_game()
    
    # if not game.games_remaining
        # go to end game (function with return 0?)
    # Show score
    
    #while guesses remaining
    while True:
        game.show_scrambled_word()
        #Show current score
        #Show remaining guesses
        game.get_player_guess()
        #game.check_if_guess_correct
            #Deduct from guesses remaining
            #Print: "Congratz" or "Incorrect"
    

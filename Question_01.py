# Author: Jamal Huraibi, fh1328
# Assignment 03
# Question 01

# General brainstorming
# 1. Load all words into a list
# 2. Shuffle the list
# 3. pop() until done
from breezypythongui import EasyFrame


class Game:
    def __init__(self):
        self.secret_word = None
        self.word_bank = None
    
    @staticmethod
    def __process_words_file():
        """Removes commas from text file. Delimits the words by SPACE and returns as List."""
        file_in_stream = open("words.txt", 'r')  # Open the in-stream file in read mode
        file_contents = file_in_stream.read()  # Store file contents as single string
        file_contents = file_contents.replace(',', '')  # Remove the commas (',')
        
        return file_contents.split()  # Return as list of individual words
    
    def initialize_game(self):
        self.word_bank = self.__process_words_file()
    
    def __shuffle_words(self):
        self.word_bank = self.word_bank
    
    def start_game(self):
        pass
    
    def get_random_word(self):
        pass
    
    def games_remaining(self):
        return len(self.word_bank)

    def test(self):
        import random
        random.shuffle(self.word_bank)
        scrambled = " ".join(self.word_bank)
        print("Shuffled: ")
        print(scrambled)


class GUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Unscramble the Word")
        self.addLabel(text="Try to unscramble the word: ", row=0, column=0)
        self.addLabel(text="Your Guess: ", row=0, column=0)


if __name__ == '__main__':
    game = Game()
    
    game.initialize_game()
    game.test()                     # testing shuffling of words (DONE - WORKING)

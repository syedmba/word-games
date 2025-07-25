import random
import json

from utils.bcolors import bcolors

from global_vars import LOG_LEVEL, LOG_DIR

from utils.key_state import KeyState

import logging

logger = logging.getLogger(__name__)

logging_dir = LOG_DIR + '/wordle.log'
logging.basicConfig(filename=logging_dir, 
                    level=LOG_LEVEL,
                    format='[%(asctime)s][%(levelname)s][%(filename)s] %(message)s')


with open('words_dictionary.json') as file:
        WORD_DICT = json.load(file)


class Wordle:
    """
    The class for the game Wordle.
    """

    def __init__(self):
        """
        Randomly selects a 5-letter word and initializes
        variables used for the game interface.
        """

        # Choose word
        global WORD_DICT
        self.word, _ = random.choice(list(WORD_DICT.items()))
        while len(self.word) != 5:
            self.word, _ = random.choice(list(WORD_DICT.items()))
        
        # Convert to uppercase
        self.word = self.word.upper()
        logger.debug(f"word = {self.word}")

        # Initialize keys
        self.keys = {x: KeyState.UNUSED for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        self.guessed = [0]*len(self.word)

        # Initalize print width
        self.game_width = 20

        self.tries_allowed = 0 #TODO

    def print_keys(self):
        """
        Prints the keys of the keyboard in QWERTY form.
        Each key has a color showing its state from:
        1. Key not used yet.
        2. Key used but not in word.
        3. Key in word and not in correct place.
        4. Key in word and in correct place.
        """
        
        keyboard_order = "QWERTYUIOPASDFGHJKLZXCVBNM"
        for k in keyboard_order:
            if k == "A":
                print("\n ", end="")
            elif k == "Z":
                print("\n   ", end="")
            if self.keys[k] == KeyState.UNUSED:
                print(f"{bcolors.OKCYAN}{k}{bcolors.ENDC}", end=" ")
            elif self.keys[k] == KeyState.PRESENT:
                print(f"{bcolors.WARNING}{k}{bcolors.ENDC}", end=" ")
            elif self.keys[k] == KeyState.CORRECT:
                print(f"{bcolors.OKGREEN}{k}{bcolors.ENDC}", end=" ")
            elif self.keys[k] == KeyState.WRONG:
                print(f"{bcolors.FAIL}{k}{bcolors.ENDC}", end=" ")
        print()

    
    def begin(self):
        """
        The complete game from start to finish.

        Takes input from user until user inputs
        the correct word or inputs "exit". At each
        iteration, calls print_keys() to print 
        the keyboard.
        """

        print("="*self.game_width)
        print(f"       Wordle")
        print("="*self.game_width)

        print(f"The word is " + "\u2610"*len(self.word))

        success = False
        tries=0
        while not success:
            
            self.print_keys()
            player_guess = input("Enter Guess: ")
            
            while True:
                if player_guess == "exit":
                    print(f"{bcolors.FAIL}Huh? Major skill issue. The word was {self.word}.{bcolors.ENDC}")
                    exit()
                if len(player_guess) != len(self.word):
                    print(f"Your guess has to be {len(self.word)} letters long !")
                    player_guess = input("Enter Guess: ")
                elif player_guess.lower() not in WORD_DICT:
                    print(f"Not a valid word !")
                    player_guess = input("Enter Guess: ")
                else:
                    break
            
            player_guess = player_guess.upper()

            print("="*self.game_width)

            correct = 0

            print(f" "*7, end="")
            for i in range(len(player_guess)):
                if player_guess[i] == self.word[i]:
                    correct += 1
                    print(f"{bcolors.OKGREEN}{player_guess[i]}{bcolors.ENDC}", end="")

                    if self.guessed[i] == 0:
                        self.keys[player_guess[i]] = KeyState.CORRECT
                        self.guessed[i] = 1

                elif player_guess[i] in self.word:
                    print(f"{bcolors.WARNING}{player_guess[i]}{bcolors.ENDC}", end="")

                    if self.keys[player_guess[i]] != KeyState.CORRECT:
                        self.keys[player_guess[i]] = KeyState.PRESENT

                else:
                    print(f"{player_guess[i]}", end="")
                    self.keys[player_guess[i]] = KeyState.WRONG
            print()
            if correct == len(self.word):
                success = True

            tries += 1
        
        print("="*self.game_width)
        print(f"{bcolors.OKGREEN}Congratulations! The word was {self.word}. You got it in {tries} tries.{bcolors.ENDC}")
        

if __name__ == "__main__":
    game = Wordle()
    game.begin()


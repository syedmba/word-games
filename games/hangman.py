import random
import json
from enum import Enum

from utils.bcolors import bcolors

from global_vars import LOG_LEVEL
from wordle import KeyState

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename='wordle.log', level=LOG_LEVEL)


with open('words_dictionary.json') as file:
        WORD_DICT = json.load(file)


class Hangman:

    def __init__(self):
        """
        Randomly selects an n-letter word and initializes
        variables used for the game interface.
        """
        # Choose word
        global WORD_DICT
        self.word, _ = random.choice(list(WORD_DICT.items()))

        # Convert to uppercase
        self.word = self.word.upper()
        logger.debug(f"word = {self.word}")

        # Initialize keys
        self.keys = {x: KeyState.UNUSED for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

        # Initalize print width
        self.game_width = 20

        # Initialize number of tries allowed
        self.max_tries = 7

    def print_keys(self):
        """
        Prints the keys of the keyboard in QWERTY form.
        Each key has a color showing its state from:
        1. Key not used yet.
        2. Key used but not in word.
        3. Key in word.
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
                raise Exception("Hangman is not supposed to utilize KeyState.PRESENT !")
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
        print(f"       Hangman")
        print("="*self.game_width)

        print(f"The word is " + "\u2610"*len(self.word))
        print(f"Remaining tries: {self.max_tries}")

        success = False
        tries=0
        while not success and tries < self.max_tries:
            
            self.print_keys()
            player_guess = input("Enter Guess: ")
            
            while True:
                if player_guess == "exit":
                    print(f"{bcolors.FAIL}Huh? Major skill issue. The word was {self.word}.{bcolors.ENDC}")
                    exit()
                if len(player_guess) != 1:
                    print(f"Your guess has to be a single character!")
                    player_guess = input("Enter Guess: ")
                elif not player_guess.isalpha():
                    print(f"Not a valid letter !")
                    player_guess = input("Enter Guess: ")
                else:
                    break
            
            player_guess = player_guess.upper()

            print("="*self.game_width)

            correct = 0

            print(f" "*7, end="")

            if player_guess in self.word:
                self.keys[player_guess] = KeyState.CORRECT
            else:
                self.keys[player_guess] = KeyState.WRONG
                tries += 1
                

            for i in range(len(self.word)):
                if self.keys[self.word[i]] == KeyState.CORRECT:
                    correct += 1
                    print(f"{bcolors.OKGREEN}{self.word[i]}{bcolors.ENDC}", end="")
                else:
                    print(f"{bcolors.FAIL}_{bcolors.ENDC}", end="")
            print()


            if correct == len(self.word):
                success = True
            
            print(f"Remaining tries: {self.max_tries - tries}")
        
        print("="*self.game_width)
        
        if success:
            print(f"{bcolors.OKGREEN}Congratulations! The word was {self.word}. You got it in {tries} tries.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}Womp womp... The word was {self.word}.{bcolors.ENDC}")

if __name__ == "__main__":
    game = Hangman()
    game.begin()
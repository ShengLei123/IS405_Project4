# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        temp_string = ''
        for x in range(0, N_COLS):
            temp_string += gw.get_square_letter(row=0, col=x)
        temp_string = temp_string.lower()
        print(temp_string)
        if temp_string in FIVE_LETTER_WORDS:
            gw.show_message("Keep guessing")
        else:
            gw.show_message("No in word list")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
    word = random.choice(FIVE_LETTER_WORDS).upper()
    
    temp_col = 0
    for x in word:
        gw.set_square_letter(row=0, col=temp_col, ch=x)
        temp_col += 1
    
    gw.add_enter_listener(enter_action)

if __name__ == "__main__":
    wordle()

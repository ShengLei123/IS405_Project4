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
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

    word = random.choice(FIVE_LETTER_WORDS).upper()
    col_num = N_COLS - 1
    row_num = N_ROWS - 1
    
    col_num = 0
    for x in word:
        gw.set_square_letter(row=0, col=col_num, ch=x)
        col_num += 1

if __name__ == "__main__":
    wordle()

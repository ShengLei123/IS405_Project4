# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    def enter_action(s):
        if len(s.replace(" ", ''))  != 5:
            gw.show_message("Please enter 5 letters")
            return True

        if s.lower() in FIVE_LETTER_WORDS:
            gw.show_message("Keep guessing")
        else:
            gw.show_message("Not in word list")

        for x in range(0, N_COLS):
            gw.set_square_color(row=gw.get_current_row(), col=x, color=MISSING_COLOR)
        
        temp_col = 0
        for x in s: 
            if x in word:
                gw.set_square_color(row=gw.get_current_row(), col=temp_col, color=PRESENT_COLOR)
                if word[temp_col] == s[temp_col]:
                    gw.set_square_color(row=gw.get_current_row(), col=temp_col, color=CORRECT_COLOR)
            temp_col += 1
            
        gw.set_current_row(gw.get_current_row()+1 if gw.get_current_row() != 5 else gw.get_current_row())

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code
    word = random.choice(FIVE_LETTER_WORDS).upper()
    
    temp_col = 0
    for x in word:
        gw.set_square_letter(row=0, col=temp_col, ch=x)
        temp_col += 1
    
    # if gw.get_square_letter(row=gw.get_current_row(), col=0) == ' ':
    #     gw.set_square_color(row=gw.get_current_row(), col=gw.get_)

if __name__ == "__main__":
    wordle()

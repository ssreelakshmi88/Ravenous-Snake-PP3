"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""

import curses

# setting window
sc = curses.initscr()
win = curses.newwin(20, 80, 0, 0)
win.keypad(1)  # to recognize the key presses
curses.noecho()  # prevents user key presses registering on terminal window

# Snake and food position

food_position = [8, 55]
snake_head = [10, 15]
snake_position = [[15, 10], [14, 10], [13, 10]]

SCORE = 0


win.addch(food_position[0], food_position[1], "█")

"""
The curses module is used to handle user keypresses,
allowing them to move the snake
"""

import curses

# setting window
sc = curses.initscr()
win = curses.newwin(20, 80, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)


# logic of playing game

#!/usr/bin/env python

import sys
import string
import time

import curses
import curses.wrapper

from ascii_hashes import *


# Print a multi-line string s to the curses window w
  # x is the column number to start on
def print_ascii( s, w, x=2 ):
    for y, line in enumerate(s.splitlines(), x):
        w.addstr(y, x, line)

def main(x):
    stdscr = curses.initscr()
    curses.noecho() # Don't echo the characters to screen
    curses.cbreak() # Don't require an ENTER (buffered mode off)
    stdscr.keypad(1) # Interpret keypad characters properly
    curses.curs_set(0) # Cursor invisible

    # Write to screen
    inpt = 100
    inpt_chr = 'a'
    while inpt_chr != '-99': # 99 should never happen since it's taking a character at a time--use Control-C to exit program
        inpt = stdscr.getch()
        try:
            inpt_chr = chr(inpt)
        except:
            inpt_chr = '-98'
        if inpt_chr in ascii_letters:
            ascii_art = ascii_letters[ string.upper( inpt_chr ) ]
            stdscr.clear() # Clear screen
            for y, line in enumerate(ascii_art.splitlines(), 4):
                stdscr.addstr(y, 4, line)

    # Terminate curses
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()


if __name__ == "__main__":
    curses.wrapper( main )

#!/usr/bin/env python3
import curses
stdscr = curses.initscr()
# dont echo pressed characters immediately
curses.noecho()
# reacting to individual key presses without the need for Enter to be pressed
curses.cbreak()
# auto processing of escape sequences
stdscr.keypad(True)

# ending line to restore terminal operation immediately
curses.endwin()

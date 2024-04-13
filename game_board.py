#!/usr/bin/env python3
# just fucking around with shit for fun anyways : 
"""
|x|o|x|
|x|x|x|
|o|x|o|
"""
from random import randint as rd
# i will use oop >~< : 
class GameBoard:
    # both x,y coords start with 1 not 0 so remember that
    # and the game board uses spaces meaning empty cells
    def __init__(self):
        # 3 by 3 game board coords start from upper left and both axis have 3 values possible 0, 1, 2
        self.game_board = [[" ", " ", " "],
                           [" ", " ", " "],
                           [" ", " ", " "]]
    def row_string(self, row):
        # convert row for index usage
        row -= 1
        return "|" + "|".join(self.game_board[row]) + "|"
    def board_string(self):
        # get row strings in an nice list then join it with \n new line
        row_strings = [self.row_string(row) for row in range(1,4)] 
        return "\n".join(row_strings)
    def set_cell(self, row, column, char):
        # convert both to indexes
        row -= 1
        column -= 1
        # True means cell was set, false means it wasnt set
        if self.game_board[row][column] == " ":
            self.game_board[row][column] = char
            return True
        else:
            return False
    def get_cell(self, row, column):
        # convert both to indexes
        row -= 1
        column -= 1
        return self.game_board[row][column]
    def reset_board(self):
        # reset the board
        self.game_board = [[" ", " ", " "],
                           [" ", " ", " "],
                           [" ", " ", " "]]
    # the hard part of checking weather game is over or not
    def is_board_full(self):
        # check if the board is full or not
        if " " in self.board_string():
            return False
        else:
            return True
    def check_win_conditions(self):
        # And return the winning character
        # check diagonals first :
        if (self.get_cell(1, 1) == self.get_cell(2, 2) == self.get_cell(3, 3)) or (self.get_cell(1, 3) == self.get_cell(2, 2) == self.get_cell(3, 1)):
            if self.get_cell(2,2) != " ":
                return self.get_cell(2, 2)
        # check rows 
        for row in range(1,4):
            if (self.get_cell(row, 1) == self.get_cell(row, 2) == self.get_cell(row, 3)):
                if self.get_cell(row, 2) != " ":
                    return self.get_cell(row, 2)
        # check columns
        for column in range(1,4):
            if (self.get_cell(1, column) == self.get_cell(2, column) == self.get_cell(3, column)):
                if self.get_cell(2, column) != " ":
                    return self.get_cell(2, column)
        # return False if no winner
        return False

def main():
    # define the board
    board = GameBoard()
    # ask the player for his choice of character
    player_char = ""
    while player_char not in ["x", "o"]:
        player_char = input("choose x or o : ").lower()
    if player_char == "x":
        game_char = "o"
    else:
        game_char = "x"
    # infinite loop until game is over
    game_over = False
    while not game_over:
        # output the board
        print(board.board_string())
        # get player rc choice
        player_rc = input("comma separated value for rows and columns (r,c) : ").split(",")
        while not board.set_cell(int(player_rc[0]), int(player_rc[1]), player_char):
            player_rc = input("comma separated value for rows and columns (r,c) : ").split(",")
            continue
        # random game cell set
        while not (board.set_cell(rd(1,3), rd(1,3), game_char) and board.is_board_full):
            continue
        if board.is_board_full():
            win_check = board.check_win_conditions()
            if win_check:
                if win_check == player_char:
                    print("congratz you won ig")
                else:
                    print("you lost")
                print(board.board_string())
            else:
                print("board's full")
                print(board.board_string())
                game_over = True
                continue
        # in case board not full
        else:
            win_check = board.check_win_conditions()
            if win_check:
                if win_check == player_char:
                    print("congratz you won")
                else:
                    print("eww you lost what a loser :3")
                game_over = True
                print(board.board_string())
                continue
            else:
                continue

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# | | | |
# | | | | :3 the game board form
# | | | |
from random import randint as rd

class GameBoard:
    def __init__(self):
        self.game_board = [[" ", " ", " "],
                           [" ", " ", " "],
                           [" ", " ", " "]]
        self.rows = range(1, 4)
        self.cols = range(1, 4)
    def row_string(self, row):
        # intermediate function for easier more separate logic
        return f"|{'|'.join(self.game_board[row-1])}|"
    def board_string(self):
        # use quick list creation method
        return "\n".join([self.row_string(i) for i in range(1,4)])
    def get_cell(self, row, col):
        return self.game_board[row - 1][col - 1]
    def set_cell(self, row, col, char):
        # just set the char no fucking checks whatsoever do the checking after keep it clean and split
        self.game_board[row - 1][col - 1] = char
    def clear_board(self):
        # clears the board
        # loop through all the rows
        for row in self.rows:
            # for each row loop cols
            for col in self.cols:
                # reset the cell
                self.set_cell(row, col, " ")
    def check_board_full(self):
        # return True for full board, False for empty board yay
        board_full = True
        # loop and if u find any empty cell set board_full to false and brakes
        for row in self.rows:
            for col in self.cols:
                if self.get_cell(row, col) == " ":
                    board_full = False
                    return board_full
        return board_full
    def check_rows_win(self):
        # its not a bug its a feature return only strings UwU if its space empty string assume its false peak design damn
        for row in self.rows:
            if self.get_cell(row, 1) == self.get_cell(row, 2) == self.get_cell(row, 3):
                return self.get_cell(row, 2)
        return " "
    def check_columns_win(self):
        # same shit but in reverse UwU
        for col in self.cols:
            if self.get_cell(1, col) == self.get_cell(2, col) == self.get_cell(3, col):
                return self.get_cell(2, col)
        return " "
    def check_cross_win(self):
        # get a list of the two crosses
        cross_one = [self.get_cell(i, i) for i in self.rows if i != 2]
        cross_center = self.get_cell(2,2)
        cross_two = [self.get_cell(1,3), self.get_cell(3,1)]
        if (cross_one[0] == cross_center == cross_one[1]) or (cross_two[0] == cross_center == cross_two[1]):
            return cross_center
        return " "
    def check_win(self):
        # check board winner returns the winning character or " " if no winner
        # collect all the win conds separately
        win_conditions = [self.check_rows_win(), self.check_cross_win(), self.check_columns_win()]
        for win_con in win_conditions:
            if win_con != " ":
                return win_con
        return " "
    def get_available_cells(self):
        available_cells = []
        for row in self.rows:
            for col in self.cols:
                if self.get_cell(row, col) == " ":
                    available_cells.append([row, col])
        return available_cells
    def is_game_over(self):
        if (self.check_win() != " ") or (self.get_available_cells() == []):
            return True
        return False

def main():
    # housekeeping stuff : 
    board = GameBoard()
    board_full = False
    board.clear_board()
    # remember to update game_run variable after every board.set_cell
    game_run = True
    # think about the turn cycle in both cases of choosing x or o
    player_char = input("x or o : ")
    while player_char not in ["x", "o"]:
        player_char = input("x or o : ")
    if player_char == "x":
        player_first = True
        game_char = "o"
    else:
        player_first = False
        game_char = "x"

    while game_run:
        # player_first turn cycle
        if player_first:
            # get player choice
            player_rc = input("r,c : ").split(",")
            while [int(player_rc[0]), int(player_rc[1])] not in board.get_available_cells():
                player_rc = input("r,c : ")
            board.set_cell(int(player_rc[0]), int(player_rc[1]), player_char)
            # check if game is over
            if board.is_game_over():
                game_run = False
                continue
            # game turn : 
            available_options = board.get_available_cells()
            game_rc = available_options[rd(0, len(available_options) - 1)]
            board.set_cell(game_rc[0], game_rc[1], game_char)
            print(board.board_string())
        # if the player isnt first
        else:
            # game rc choice
            available_options = board.get_available_cells()
            game_rc = available_options[rd(0, len(available_options) - 1)]
            board.set_cell(game_rc[0], game_rc[1], game_char)
            print(board.board_string())
            # check if game is over
            if board.is_game_over():
                game_run = False
                continue
            # get player choice
            player_rc = input("r,c : ").split(",")
            while [int(player_rc[0]), int(player_rc[1])] not in board.get_available_cells():
                player_rc = input("r,c : ")
            board.set_cell(int(player_rc[0]), int(player_rc[1]), player_char)
            print(board.board_string())
        # check for board over one more time
        if board.is_game_over():
            game_run = False
            continue

    # print the winner
    board_winner = board.check_win()
    if board_winner == player_char:
        print("you won")
    elif board_winner == game_char:
        print("you lost")
    else:
        print("tie")
    print(board.board_string())
if __name__ == "__main__":
    main()

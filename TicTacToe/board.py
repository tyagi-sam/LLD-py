from typing import List
from collections import namedtuple

Pair = namedtuple('Pair', ['row', 'column'])

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row, column, playing_piece):
        if self.board[row][column] is not None:
            return False
        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self) -> List[Pair]:
        free_cells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append(Pair(i, j))
        return free_cells

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(self.board[i][j].pieceType.name, end="   ")
                else:
                    print("    ", end="")

                print(" | ", end="")
            print()

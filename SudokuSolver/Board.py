from SudokuSolver import Cell


class Board:
    def __init__(self):
        self.board = [[Cell.Cell(r, c) for r in range(9)] for c in range(9)]

    def set_number(self, number, row, col):
        self.board[row][col].set_number(number)

    def get_number(self, row, col):
        return self.board[row][col].get_number()

    def clear(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c].set_number(0)

    def is_valid(self, row, col, number):
        for i in range(9):
            if self.board[i][col].get_number() == number and i != row \
                    or self.board[row][i].get_number() == number and i != col:
                return False

        # Written by Orion Koepke to check a cell's block
        for r in range(row - (row % 3), row + (3 - (row % 3))):
            for c in range(col - (col % 3), col + (3 - (col % 3))):
                if c != col and r != row:
                    if self.board[r][c].get_number() == number:
                        return False
        return True

    def solve(self):
        for r in range(9):
            for c in range(9):
                pass

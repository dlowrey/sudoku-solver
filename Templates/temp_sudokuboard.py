from Solver.Cell import Cell
import os


class SudokuBoard(object):
    def __init__(self):
        # Make a 9x9 matrix of Cell objects
        self.game_board =[]

    def get_cell(self, row, column):
        """Get a specific cell on the board"""

    def clear_board(self):
        """Reset all board cells"""


    def find_possible_cell_numbers(self, cell):
        """Get ALL possible numbers that can go in the current cell

        :arg cell: the current cell to get possible numbers for
        :return a set of possible numbers for the passed cell
        """

        row = cell.get_row()
        column = cell.get_column()
        existing_numbers = set()
        valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        # Find numbers existing in this cell's effected column and row


        # Find numbers existing in this cell's effected box


        # Set the cells possible numbers to 
        # nmbers that are not in existing_numbers
        cell.set_possible_numbers(valid - existing_numbers)

    def validate_board(self):

        # Check all rows and columns
        # Return false if violations are found
        # Your code here
        return True

    def solve(self):
        """
        Place a valid number in each cell in the board
        refer to the lecture slides for algorithm
        :return: False if the board is not valid or is unsolvable,
                True otherwise
        """

        if not self.validate_board():
            return False

        # your code here

        return True

    def __str__(self):
        res = ""
        for r in range(9):
            res += '\n'
            for c in range(9):
                res += str(self.get_cell(r, c).get_number())
                res += ' '
        return res

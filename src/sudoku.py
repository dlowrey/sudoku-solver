from time import time


class Cell(object):
    """
    Representation of an individual Cell inside of a Sudoku Board
    """

    def __init__(self, row, column):
        self.row = row  # the row that this cell is in
        self.column = column  # the column that this cell is in
        self.exhausted = False  # Flag to check if we have tried all numbers
        self.number = 0  # Initial number (not valid in Sudoku)
        self.possible_numbers = set()  # Initial set of possible numbers

    def try_new_number(self):
        """
        Attempt to place a new untried number in this cell,
        and update the exhausted flag.
        """
        self.number = self.possible_numbers.pop()
        self.exhausted = not self.possible_numbers

    def set_possible_numbers(self, numbers):
        """Set the possible numbers of this cell"""
        self.possible_numbers = numbers
        self.exhausted = not numbers

    def reset_number(self):
        """Reset the number only on this cell (for backtracking)"""
        self.number = 0

    def reset(self):
        """Reset this cell completely (used if no possible numbers are found)"""
        self.exhausted = False
        self.possible_numbers = set()
        self.number = 0


class Board(object):
    """
    Representation of a 9x9 Sudoku board and the required methods to
    solve and verify one.
    """

    def __init__(self):
        # Initialize a 9x9 matrix of Cell objects
        self.board = [[Cell(r, c) for c in range(9)] for r in range(9)]

    @staticmethod
    def __difference(numbers):
        """Get the remaining usable Sudoku numbers given a list of numbers"""
        # Note that sets are unordered
        return set(range(1, 10)) - set(numbers)

    @staticmethod
    def __validate(numbers):
        """
        Discover if a section on the board is considered valid, i.e.
        follows the rules of Sudoku
        :param numbers: the list of numbers to check
        :return: boolean True if valid, False otherwise
        """
        numbers = list(filter(lambda n: n != 0, numbers))  # remove all 0s
        correct_numbers = set(numbers).issubset(set(range(1, 10)))
        no_duplicates = len(numbers) == len(set(numbers))
        return correct_numbers and no_duplicates

    def __get_row(self, row):
        """Get a row of numbers for the specified row"""
        return [cell.number for cell in self.board[row]]

    def __get_column(self, column):
        """Get a column of numbers for the specified column"""
        return [self.board[row][column].number for row in range(9)]

    def __get_square(self, row, column):
        """
        Get a 3x3 square of cells in the board that the specified cell
        belongs to.
        :param row: the row of the designated cell
        :param column: the column of the designated cell
        :return: a 3x3 matrix
        """
        return [
            self.board[r][c].number
            for r in range(row - (row % 3), row + (3 - (row % 3)))
            for c in range(column - (column % 3), column + (3 - (column % 3)))
        ]

    def is_valid(self):
        """
        Validate the entire board by checking each individual row,
        column, and square against Sudoku rules.
        :return: boolean True if valid, False otherwise
        """
        columns = [self.__validate(self.__get_column(column))
                   for column in range(9)]
        rows = [self.__validate(self.__get_row(r))
                for r in range(9)]
        squares = [
            self.__validate(self.__get_square(row, column))
            for row in range(0, 9, 3)
            for column in range(0, 9, 3)
        ]
        return all(columns + rows + squares)

    def possible_numbers(self, r, c):
        """
        Get a set of valid possible numbers for a cell at row r, column c
        :param r: row of the specified cell
        :param c: column of the specified cell
        :return: a set of possible valid numbers
        """
        row = self.__get_row(r)
        column = self.__get_column(c)
        square = self.__get_square(r, c)
        return self.__difference(row + column + square)

    def solve(self):
        """
        Solve a 9x9 Sudoku Puzzle by using Brute Force (backtracking) algorithm.
        :return: True if the puzzle was solved, False otherwise
        """
        # Check if the initial board is valid
        if self.is_valid():
            start = time()
            # Initialize a list that will hold all of the cells that we have
            # attempted to place a number in. This list will be used to
            # backtrack and try a different number in a cell.
            attempted_cells = []
            row = 0
            while row < 9:
                column = 0
                while column < 9:
                    cell = self.board[row][column]
                    backtracking = False
                    if not cell.number:  # if the cell's number is 0

                        # Check that this cell is not exhausted (i.e. all
                        # numbers have been tried) or that it does not already
                        # have a list of possible numbers.
                        if not cell.exhausted and not cell.possible_numbers:
                            # Find and set the possible numbers,
                            # because this is a set(), it may be
                            # unordered
                            possible = self.possible_numbers(row, column)
                            cell.set_possible_numbers(possible)

                        # If the cell has possible numbers, try one
                        if cell.possible_numbers:
                            cell.try_new_number()
                            attempted_cells.append(cell)

                        # Otherwise we must back track to the previous cell
                        elif attempted_cells:
                            backtracking = True
                            cell.reset()  # complete reset this cell
                            prev_cell = attempted_cells.pop(-1)
                            prev_cell.reset_number()  # clear number
                            # Set the row and column of the loops back
                            # to this cell to try it again
                            row = prev_cell.row
                            column = prev_cell.column

                        # Otherwise there are no possible solutions
                        else:
                            return False, -1

                    # If we are not going to backtrack, simply
                    # advance to the next column
                    if not backtracking:
                        column += 1

                # After we have gone through all columns,
                # advance to the next row and repeat
                row += 1

            # All cells have been fit successfully
            end = time()  # finishing time
            return True, end - start

        # The initial puzzle was not valid
        else:
            return False, -1

    def clear(self):
        [self.board[r][c].reset() for c in range(9) for r in range(9)]

    def __str__(self):
        """Return a pretty version of the board object for printing"""
        pretty = ""
        for i in range(9):
            pretty += str(self.__get_row(i))
            pretty += "\n"
        return pretty

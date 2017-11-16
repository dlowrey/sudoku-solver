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

        # Have all numbers been tried?
        if len(self.possible_numbers) == 0:
            self.exhausted = True

    def set_possible_numbers(self, numbers):
        """Set the possible numbers of this cell"""
        self.possible_numbers = numbers

        # Have all numbers been tried, resulting in
        # no more possible numbers for this cell?
        if len(numbers) == 0:
            self.exhausted = True

    def reset_number(self):
        """Reset the number only on this cell (for backtracking)"""
        self.number = 0

    def reset(self):
        """
            Reset this cell completely, except for its position
            (used if no possible numbers are found)
        """
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
        self.board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append((Cell(i, j)))
            self.board.append(row)

    @staticmethod
    def difference(numbers):
        """Get the remaining usable Sudoku numbers given a list of numbers"""
        # Note that sets are unordered
        sudoku_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        diff = sudoku_numbers - set(numbers)
        return diff

    @staticmethod
    def validate(numbers):
        """
        Discover if a section on the board is considered valid, i.e.
        follows the rules of Sudoku
        :param numbers: the list of numbers to check
        :return: boolean True if valid, False otherwise
        """
        # remove all 0s
        sudoku_numbers = []
        for num in numbers:
            if num != 0:
                sudoku_numbers.append(num)

        # check if only correct numbers are left (1-9)
        check_correct = set(sudoku_numbers).issubset({1, 2, 3, 4, 5, 6, 7, 8, 9})
        # check that there are no duplicate numbers
        check_duplicates = len(sudoku_numbers) == len(set(sudoku_numbers))
        # everything is valid if the above two are true
        valid = check_correct and check_duplicates
        return valid

    def get_row(self, row):
        """Get a row of numbers for the specified row"""
        r = self.board[row]
        row_numbers = []
        for cell in r:
            cell_num = cell.number
            row_numbers.append(cell_num)
        return row_numbers

    def get_column(self, column):
        """Get a column of numbers for the specified column"""
        column_numbers = []
        for row in range(9):
            col = self.board[row][column]
            num = col.number
            column_numbers.append(num)
        return column_numbers

    def get_square(self, row, column):
        """
        Get a 3x3 square of cells in the board that the specified cell
        belongs to.
        :param row: the row of the designated cell
        :param column: the column of the designated cell
        :return: a 3x3 matrix
        """
        square = []

        for r in range(row - (row % 3), row + (3 - (row % 3))):
            for c in range(column - (column % 3), column + (3 - (column % 3))):
                cell = self.board[r][c]
                num = cell.number
                square.append(num)

        return square

    def is_valid(self):
        """
        Validate the entire board by checking each individual row,
        column, and square against Sudoku rules.
        :return: boolean True if valid, False otherwise
        """
        column_valid = True
        for r in range(9):
            column = self.get_column(r)
            valid = self.validate(column)
            column_valid = column_valid and valid

        row_valid = True
        for r in range(9):
            row = self.get_row(r)
            valid = self.validate(row)
            row_valid = row_valid and valid

        square_valid = True
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                square = self.get_square(r, c)
                valid = self.validate(square)
                square_valid = square_valid and valid

        return column_valid and row_valid and square_valid

    def possible_numbers(self, r, c):
        """
        Get a set of valid possible numbers for a cell at row r, column c
        :param r: row of the specified cell
        :param c: column of the specified cell
        :return: a set of possible valid numbers
        """
        row = self.get_row(r)
        column = self.get_column(c)
        square = self.get_square(r, c)
        return self.difference(row + column + square)

    def solve(self):
        """
        Solve a 9x9 Sudoku Puzzle by using Brute Force (backtracking) algorithm.
        You may verify the solution at https://www.sudoku-solutions.com/
        :return: True and the time if the puzzle was solved, False and -1
                 otherwise
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
        """Reset all cells on the board"""
        for r in range(9):
            for c in range(9):
                self.board[r][c].reset()

    def __str__(self):
        """Return a pretty version of the board object for printing"""
        pretty = ""
        for i in range(9):
            pretty += str(self.get_row(i))
            pretty += "\n"
        return pretty

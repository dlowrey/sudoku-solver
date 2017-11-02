class Cell(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.exhausted = False
        self.number = 0
        self.possible_numbers = set()

    def row(self):
        return self.row

    def column(self):
        return self.column

    def exhausted(self):
        return self.exhausted

    def number(self):
        return self.number

    def possible_numbers(self):
        return self.possible_numbers

    def try_new_number(self):
        self.number = self.possible_numbers.pop()
        self.exhausted = not self.possible_numbers

    def set_possible_numbers(self, numbers):
        self.possible_numbers = numbers
        self.exhausted = not numbers

    def reset_number(self):
        self.number = 0

    def reset(self):
        self.exhausted = False
        self.possible_numbers = set()
        self.number = 0


class Board(object):
    """
    Representation of a 9x9 Sudoku board
    """

    def __init__(self):
        self.board = [[Cell(r, c) for c in range(9)] for r in range(9)]

    def __flatten(self, matrix):
        return [item for sublist in matrix for item in sublist]

    def __difference(self, numbers):
        return set(numbers) - set(i for i in range(9))

    def __validate(self, numbers):
        valid = set(numbers) == set(range(1, 10)) or set(numbers) == {0}
        return valid

    def __get_row(self, row):
        return [cell.number() for cell in self.board[row]]

    def __get_column(self, column):
        """
        Check to see if a column in the board is valid
        :param column: the column to validate
        :return: Boolean 
        """
        column = [self.board[row][column].number() for row in range(9)]
        return column

    def __get_square(self, row, column):
        square = [
            self.board[r][c].number()
            for r in range(row - (row % 3), row + (3 - (row % 3)))
            for c in range(column - (column % 3), column + (3 - (column % 3)))
        ]
        return square

    def is_valid(self):
        columns = [self.__validate(self.__get_column(column))
                   for column in range(9)]
        rows = [self.__validate(self.__get_row(r))
                for r in range(9)]
        squares = [
            self.__validate(self.__get_square(row, column))
            for row in range(0, 9, 3)
            for column in range(0, 9, 3)
        ]
        return all(self.__flatten(columns + rows + squares))

    def possible_numbers(self, r, c):
        row = self.__get_row(r)
        column = self.__get_column(c)
        square = self.__get_square(r, c)
        return self.__difference(row + column + square)

    def solve(self):
        if self.is_valid():
            attempted_cells = []
            row = 0
            while row < 9:
                column = 0
                while column < 9:
                    cell = self.board[row][column]
                    backtracking = False
                    if not cell.number():

                        if not cell.possible_numbers() and not cell.exhausted():
                            possible = self.possible_numbers(row, column)
                            cell.set_possible_numbers(possible)

                        if cell.possible_numbers():
                            cell.try_new_number()
                            attempted_cells.append(cell)

                        elif attempted_cells:
                            backtracking = True
                            cell.reset()
                            prev_cell = attempted_cells.pop(-1)
                            prev_cell.reset_number()
                            row = prev_cell.row()
                            column = prev_cell.column()

                        else:
                            return False

                    if not backtracking:
                        column += 1

                row += 1

            return True
        
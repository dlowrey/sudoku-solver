class Cell(object):
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.exhausted = False
        self.number = 0


class Board(object):
    """
    Representation of a 9x9 Sudoku board
    """

    def __init__(self):
        self.board = [[0 for i in range(9)] for i in range(9)]  # 9x9 empty

    def __flatten(self, matrix):
        return [item for sublist in matrix for item in sublist]

    def __difference(self, numbers):
        return list(set(numbers) - set(i for i in range(9)))

    def __validate(self, numbers):
        valid = set(numbers) == set(range(1, 10)) or set(numbers) == {0}
        return valid

    def __get_row(self, row):
        return self.board[row]

    def __get_column(self, column):
        """
        Check to see if a column in the board is valid
        :param column: the column to validate
        :return: Boolean 
        """
        column = [self.board[row][column] for row in range(9)]
        return column

    def __get_square(self, row, column):
        square = [
            self.board[r][c]
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

    def potential_numbers(self, r, c):
        row = self.__get_row(r)
        column = self.__get_column(c)
        square = self.__get_square(r, c)
        return self.__difference(row + column + square)

    def solve(self):
        if self.is_valid():
            current_row = 0
            while current_row < 9:
                current_column = 0
                while current_column < 9:
                    pass

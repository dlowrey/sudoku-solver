class Cell(object):
    def __init__(self, row, column):
        # Set this cell's position on the board
        self.row = row
        self.column = column
        # Set the number in the cell to 0
        self.number = 0
        # Boolean flag for if all numbers have been tried in cell
        self.exhausted = False
        # Set all possible numbers this cell can be
        self.possible_numbers = set()

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

    def set_number(self, new_number):
        self.number = new_number

    def get_number(self):
        return self.number

    def set_possible_numbers(self, possible):
        self.possible_numbers = possible

    def get_possible_numbers(self):
        return self.possible_numbers

    def has_number(self):
        return self.number != 0

    def try_number(self):
        """Try the next possible number in this cell

        Tries the first number in `self.possible_numbers`
        by popping it from the set. Once it has tried all
        of it's possible numbers, the set will be empty and
        the `exhausted` flag will become True, telling
        the solver that no solution was found for this cell.
        """
        # Try a number and remove it from possible numbers
        self.number = self.possible_numbers.pop()
        # Set the exhausted flag
        self.exhausted = self.possible_numbers == set()

    def is_exhausted(self):
        return self.exhausted

    def reset_cell(self):
        """Reset the cell to brand new

        Using `reset_cell` will lose all track of
        what numbers were tried in the cell previously.
        This is used when the cell is completely backtracked over
        """
        self.number = 0
        self.possible_numbers = set()
        self.exhausted = False

    def backtrack(self):
        """Gets the cell ready to be backtracked to"""
        self.number = 0

    def __str__(self):
        return "Cell [{}][{}]\n" \
               "Possible: {}\n" \
               "Exhausted: {}\n"\
               "Number: {}\n\n".format(
                self.row,
                self.column,
                self.possible_numbers,
                self.exhausted,
                self.number
        )

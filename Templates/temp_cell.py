class Cell(object):
    def __init__(self, row, column):
        # Variable to hold the cell's row (initialize to row)
        self.row = row
        # Variable to hold the cell's column (initialize to column)

        # Variable to hold cell's number (initialize to 0)

        # Boolean flag for if all numbers have been tried in cell (init False)

        # Variable to hold the set of all possible numbers (init empty)

    def get_row(self):
        """Returns the row of the cell"""

    def get_column(self):
        """Returns the column of the cell"""

    def set_number(self, new_number):
        """Sets the number of the cell"""

    def get_number(self):
        """Returns the number of the cell"""

    def set_possible_numbers(self, possible):
        """Sets the possible numbers for the cell"""

    def get_possible_numbers(self):
        """Returns the possible numbers of the cell"""

    def has_number(self):
        """Returns boolean of whether or not the cell has number (1-9)"""

    def try_number(self):
        """Try the next possible number in this cell

        Tries the first number in `self.possible_numbers`
        by popping it from the set. Once it has tried all
        of it's possible numbers, the set will be empty and
        the `exhausted` flag will become True, telling
        the solver that no solution was found for this cell.
        """
        # Try a number and remove it from possible numbers
        # Set the exhausted flag

    def is_exhausted(self):
        """Returns boolean of whether or not the cell has any 
            possible numbers left to try"""

    def reset_cell(self):
        """Reset the cell to brand new

        Using `reset_cell` will lose all track of
        what numbers were tried in the cell previously.
        This is used when the cell is completely backtracked over
        """


    def backtrack(self):
        """Gets the cell ready to be backtracked to"""

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

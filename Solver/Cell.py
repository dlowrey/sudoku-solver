class Cell(object):
    def __init__(self, row, column):
        # Set this cell's position on the board
        self.row = row
        self.column = column
        # Set the number in the cell to 0
        self.number = 0
        # Set all possible numbers this cell can be
        self.possible_numbers = []
        self.next_number_pointer = 0

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
        """Try the next untried number in the cell
        try_number will fit it's cell with a number in
        `possible_numbers` at index 0 always.
        """
        if len(self.possible_numbers) > self.next_number_pointer:
            number = self.possible_numbers[self.next_number_pointer]
            self.number = number
            self.next_number_pointer += 1

    def reset_cell(self):
        """Reset the cell to brand new

        Using `reset_cell` will lose all track of
        what numbers were tried in the cell previously.
        This should only be used on cell's where `possible_numbers` == []
        when we first tried to put a number in them.
        """
        self.number = 0
        self.next_number_pointer = 0
        self.possible_numbers = []

    def backtrack(self):
        self.number = 0

    def __str__(self):
        return "Cell [{}][{}]\n" \
               "Possible: {}\n" \
               "Idx: {}\n" \
               "Number: {}\n\n".format(
                self.row,
                self.column,
                self.possible_numbers,
                self.next_number_pointer,
                self.number
        )

class Cell:
    def __init__(self, row, col):
        # the cell's position on the board
        self.row = row
        self.col = col
        # the cell's starting number (0 is 'empty')
        self.number = 0
        # list of numbers (1 - 9) that could potentially be
        # the cell's number without breaking sudoku rules
        self.possible_numbers = []
        # The indexer that is used to advance through
        # each of this cell's possible_numbers (will be reset if the cell is backtracked over)
        self.number_idx = -1

    # get the number of this cell
    def _get_number(self):
        return self.number

    # set the number of this cell
    def set_number(self, number):
        self.number = number

    # check if this cell has a possible number
    def _has_number_to_try(self):
        return self.number_idx < (len(self.possible_numbers) - 1)

    # try the next possible number in this cell
    def _try_next_number(self):
        self.number_idx += 1
        self.number = self.possible_numbers[self.number_idx]


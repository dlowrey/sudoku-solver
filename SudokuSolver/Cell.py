class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.number = 0
        self.possible_numbers = []
        self.numbers_tried = []
        self.number_idx = -1

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def has_possible_number(self):
        return self.number_idx < (len(self.possible_numbers) - 1)

    def try_next_number(self):
        self.number_idx += 1
        self.number = self.possible_numbers[self.number_idx]


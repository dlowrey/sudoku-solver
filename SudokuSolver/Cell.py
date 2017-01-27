

class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.number = 0
        self.possible_numbers = [i+1 for i in range(9)]
        self.number_idx = -1

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number

    def tryNextNumber(self):
        self.set_number(self.possible_numbers[self.number_idx++ + 1])

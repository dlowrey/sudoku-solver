from Solver.Cell import Cell
import os
class SudokuBoard(object):

    def __init__(self):
        # Make a 9x9 matrix of Cell objects
        self.game_board = [[Cell(row, column) for column in range(9)] for row in range(9)]

    def get_cell(self, row, column):
        return self.game_board[row][column]

    def clear_board(self):
        for row in range(9):
            for column in range(9):
                self.get_cell(row, column).reset_cell()

    def find_possible_cell_numbers(self, cell):
        """Get ALL possible numbers that can go in the current cell

        :arg cell: the current cell to get possible numbers for
        :return a set of possible numbers for the passed cell
        """

        row = cell.get_row()
        column = cell.get_column()
        effected_cells = set()
        valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        # Find numbers existing in this cell's effected column and row
        for x in range(9):
            if x != row:
                effected_cells.add(self.get_cell(x, column).get_number())
            if x != column:
                effected_cells.add(self.get_cell(row, x).get_number())
        # Find numbers existing in this cell's effected box
        for r in range(row - (row % 3), row + (3 - (row % 3))):
            for c in range(column - (column % 3), column + (3 - (column % 3))):
                if c != column and r != row:
                    effected_cells.add(self.get_cell(r, c).get_number())

        # Return a list of numbers that are not in `effected_cells`
        return valid - effected_cells

    def solve(self):
        cells_tried = []
        row = 0
        while row < 9:
            column = 0
            while column < 9:
                cell = self.get_cell(row, column)

                # Check if cell needs filled
                if not cell.has_number():

                    # Find it's possible numbers if it has none
                    #  and it has not tried all of them
                    if not cell.get_possible_numbers() and not cell.is_exhausted():
                        cell.set_possible_numbers(
                            self.find_possible_cell_numbers(cell))
                
                    if cell.get_possible_numbers():
                        cell.try_number()
                        cells_tried.append(cell)
                        column += 1
                    elif cells_tried:
                        # Start over with this cell
                        cell.reset_cell()
                        # Get the previous cell
                        previous_cell = cells_tried[-1]
                        # ONLY reset the previous cell's number
                        previous_cell.backtrack()
                        cells_tried.remove(previous_cell)
                        # Set the loop back to try the `previous_cell`
                        row = previous_cell.get_row()
                        column = previous_cell.get_column()

                    else:
                        return False
                else:
                    column += 1
            row += 1
        return True



    def __str__(self):
        res = ""
        for r in range(9):
            res += '\n'
            for c in range(9):
                res += str(self.get_cell(r,c).get_number())
                res += ' '
        return res

    def save_to_file(self):
        file = open('sudoku-solution.txt', 'w')
        res = ""
        for r in range(9):
            for c in range(9):
                res += str(self.get_cell(r,c).get_number())
        file.write(res)
        file.close()

    def load_from_file(self):
        file_path = input("Please input the path to your file: ")
        file = open(os.path.join(file_path), 'r')
        number_line = file.read()
        file.close()

        for pos, num in enumerate(number_line):
            row = pos // 9
            col = pos % 9
            if num.isdigit():
                self.get_cell(row, col).set_number(int(num))














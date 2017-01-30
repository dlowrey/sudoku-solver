from SudokuSolver import Cell


class Board:
    def __init__(self):
        self.board = [[Cell.Cell(r, c) for c in range(9)] for r in range(9)]


    def set_number(self, number, row, col):
        self.board[row][col].set_number(number)

    def get_number(self, row, col):
        return self.board[row][col].get_number()

    def clear(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c].set_number(0)

    def __find_possible(self, row, col):
        effected_row = []
        effected_col = []
        effected_box = []
        for i in range(9):
            if i != row:
                effected_col.append(self.board[i][col].get_number())
            if i != col:
                effected_row.append(self.board[row][i].get_number())

        # Written by Orion Koepke to check a cell's block
        for r in range(row - (row % 3), row + (3 - (row % 3))):
            for c in range(col - (col % 3), col + (3 - (col % 3))):
                if c != col and r != row:
                    effected_box.append(self.board[r][c].get_number())
        solution = []
        # for x in range(9):
        #     x += 1
        #     if x not in effected_row and x not in effected_col and x not in effected_box:
        #         solution.append(x)

        return [i + 1 for i in range(9) if i + 1 not in effected_row\
                and i + 1 not in effected_col\
                and i + 1 not in effected_box]


    def solve(self):
        cells_tried = []
        row = 0
        while row < 9:
            col = 0
            while col < 9:
                # Grab the cell and find it's possible numbers
                this_cell = self.board[row][col]
                # print("CELL: ", row, col)
                if this_cell.get_number() == 0:
                    # Find the cell's possible numbers
                    this_cell.possible_numbers = self.__find_possible(row, col)
                    # print("POSSIBLE NUMBERS: ", this_cell.possible_numbers)
                    if this_cell.has_possible_number():
                        # Fit one of the possible numbers
                        this_cell.try_next_number()
                        # print(this_cell.get_number(), " WORKED!")
                        # Add cell to cells_tried
                        cells_tried.append(this_cell)
                        # advance
                        col += 1
                    elif len(cells_tried) > 0:
                        # print("BACKTRACKING------------------------------------")
                        this_cell.number_idx = -1
                        # Get the previous cell we fitted
                        prev_cell = cells_tried[-1]
                        # Undo the guess
                        prev_cell.set_number(0)
                        # Remove from cells_tried
                        cells_tried.remove(prev_cell)
                        # print("PREVIOUS CELL: ", prev_cell.row, prev_cell.col)
                        row = prev_cell.row
                        col = prev_cell.col
                    else:
                        # print("Unsolvable, ended on cell ", row, col)
                        return False

                else:
                    col += 1
            row += 1
        return True




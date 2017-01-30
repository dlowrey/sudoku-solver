from SudokuSolver import Cell


class Board:
    def __init__(self):
        # fill a 9x9 matrix with empty cells
        self.board = [[Cell.Cell(r, c) for c in range(9)] for r in range(9)]

    # set a cell's number (used in GUI because Board.py object cannot be indexed)
    def _set_number(self, number, row, col):
        self.board[row][col]._set_number(number)

    # get a cell's number (used in GUI because Board.py object cannot be indexed)
    def _get_number(self, row, col):
        return self.board[row][col]._get_number()

    # clear the entire board (all cell.number set to 0)
    def _clear(self):
        for r in range(9):
            for c in range(9):
                this_cell = self.board[r][c]
                this_cell._set_number(0)
                this_cell.number_idx = -1

    # find all possible numbers that could be in a cell without
    # breaking sudoku rules
    def _find_possible(self, row, col):
        effected_row = []
        effected_col = []
        effected_box = []

        # Find numbers existing in the cell's effected column and row
        for i in range(9):
            if i != row:
                effected_col.append(self.board[i][col]._get_number())
            if i != col:
                effected_row.append(self.board[row][i]._get_number())

        # Written by Orion Koepke to check a cell's effected block
        for r in range(row - (row % 3), row + (3 - (row % 3))):
            for c in range(col - (col % 3), col + (3 - (col % 3))):
                if c != col and r != row:
                    effected_box.append(self.board[r][c]._get_number())

        # solution = []
        # for x in range(9):
        #     x += 1
        #     if x not in effected_row and x not in effected_col and x not in effected_box:
        #         solution.append(x)
        # return solution

        # return a list containing numbers 1 through 9 that do not appear in
        # any of the effected_xxx lists
        return [i + 1 for i in range(9) if i + 1 not in effected_row\
                and i + 1 not in effected_col\
                and i + 1 not in effected_box]


    # solve(self)
    # Brute force backtracking algorithm O(n^2)
    # For each cell the algorithm:
    #   1) See if cell is blank (i.e cell.number == 0)
    #       2) find all possible numbers that could go in the cell (see self.__find_possible(row, col))
    #       3) if there is a possible number that could fill the cell,
    #           3a. put the number in the cell and put the cell in 'cells_tried' (a list of cell's that we have filled already)
    #           3b. advance "col"
    #       4) else if cells_tried is not empty
    #           4a. reset the current cell's number index (because it could potentially get new "possible_numbers" when we reach it again
    #           4b. get the last cell out of cells_tried and set clear it's number (i.e. set it to 0)
    #           4c. remove the cell obtained in 4b from cells_tried
    #           4d. set the loop back to the previous cell obtained in 4b and try it's next possible number
    #               4d comment: trying the next number for the cell obtained in 4b will just get the same possible_numbers but
    #                           this time the cell's number_idx will be +1 of the previous time we tried to fit it
    #       5) else the puzzle is unsolvable
    #   6) else advance col
    def solve(self):
        cells_tried = []
        row = 0
        while row < 9:
            col = 0
            while col < 9:
                # Grab the cell and find it's possible numbers
                this_cell = self.board[row][col]
                # print("CELL: ", row, col)
                if this_cell._get_number() == 0:

                    if len(this_cell.possible_numbers) == 0:
                        # this will be true if it's the first time visiting the cell
                        # or if we have backtracked and come up back to the cell
                        # Find the cell's possible numbers
                        this_cell.possible_numbers = self._find_possible(row, col)
                    # print("POSSIBLE NUMBERS: ", this_cell.possible_numbers)


                    if this_cell._has_possible_number():
                        # Fit one of the possible numbers
                        this_cell._try_next_number()
                        # print(this_cell.get_number(), " WORKED!")
                        # Add cell to cells_tried
                        cells_tried.append(this_cell)
                        # advance
                        col += 1

                    elif len(cells_tried) > 0:
                        # print("BACKTRACKING------------------------------------")
                        # Reset this cell as if we have never touched it
                        this_cell.number_idx = -1
                        this_cell.possible_numbers = []
                        # Get the previous cell we fitted
                        prev_cell = cells_tried[-1]
                        # Undo its guess
                        prev_cell._set_number(0)
                        # Remove it from cells_tried
                        cells_tried.remove(prev_cell)
                        # print("PREVIOUS CELL: ", prev_cell.row, prev_cell.col)
                        # set the loop back to its location to attempt a new number
                        row = prev_cell.row
                        col = prev_cell.col

                    else:
                        # print("Unsolvable, ended on cell ", row, col)
                        return False



                else:
                    col += 1
            row += 1
        return True




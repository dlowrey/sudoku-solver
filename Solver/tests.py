from Solver.Cell import Cell
from Solver.SudokuBoard import SudokuBoard


board = SudokuBoard()
load = input("Would you like to load a board?(Y,N): ")
if load == "Y":
    board.load_from_file()


def test_find_possible_cell_numbers():
    """
    use only when board is blank
    :return:
    """
    for row in range(9):
        for column in range(9):
            cell = board.get_cell(row, column)
            possible_numbers = board.find_possible_cell_numbers(cell)
            if possible_numbers != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("Error finding possible numbers for cell [{}][{}]".format(
                    row, column))
                return
    print("TESTS: Possible cell numbers OK")


def test_board_solved():
    # board.solve()

    numbers_seen_row = set()
    numbers_seen_column = set()
    number_seen_box = set()
    valid = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for row in range(9):
        for column in range(9):
            numbers_seen_row.add(board.get_cell(row, column).get_number())
            numbers_seen_column.add(board.get_cell(column, row).get_number())

            for r in range(row - (row % 3), row + (3 - (row % 3))):
                for c in range(column - (column % 3),
                               column + (3 - (column % 3))):
                    if c != column and r != row:
                        number_seen_box.add(board.get_cell(row,
                                                           column).get_number())

        if numbers_seen_row != valid or\
                numbers_seen_column != valid:
            print("Error, board solve is not valid")
            return

        numbers_seen_row.clear()
        numbers_seen_column.clear()
    print("TESTS: Board solution is valid")
    print(board)

    # Check solutions by uploading the file to
    # https://www.sudoku-solutions.com/
    # using the 'load' button and then clicking 'check'
    save = input("Save to file? (Y/N):")
    if save == "Y":
        board.save_to_file()







if __name__ == '__main__':
    test_board_solved()
from os import path, listdir, mkdir

"""
Writes and Reads sudoku boards from .txt files in the same format used
by www.sudoku-solutions.com for third party verification and sudoku board
generation.
"""

DATA_DIR = "../data/"


def ensure_data_dir():
    """
      Check to see if the data directory exists.
      If not, create it
      """
    data_dir = path.normpath(DATA_DIR)
    if not path.isdir(data_dir):  # check for existence
        mkdir(data_dir)  # create


def write(board):
    """
    Write a board object to a .txt. file.
    
    Formatting: each cell is represented by its number. If the cell
                does not have a number it is represented by a 0
    :param board: the board to write to a text file
    """
    ensure_data_dir()
    try:
        # create file name
        name = DATA_DIR + "saved-board"
        # count how many files are in the data folder
        number = len([f for f in listdir('../data/') if path.isfile(f)])
        name += str(number) + ".txt"
        # create file
        file = open(name, 'w')
        out = ""
        for r in range(9):
            for c in range(9):
                cell = board.board[r][c]
                number = cell.number
                out += number
        file.write(out)
        file.close()
    except FileNotFoundError as e:
        print(e)

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
    path = ""
    try:
        # create file name
        name = DATA_DIR + "saved-board"
        # count how many entries are in the data folder
        number = len(listdir(DATA_DIR))
        name += str(number) + ".txt"
        # create file
        file = open(name, 'w')
        out = ""
        for r in range(9):
            for c in range(9):
                cell = board.board[r][c]
                number = cell.number
                out += str(number)
        file.write(out)
        path = name
        file.close()
    except FileNotFoundError as e:
        print(e)
    return path


def load(file_path):
    """
    Load a sudoku board from a file path given

    Formatting: each character is its integer representation or the integer
                0 if the character is not a digit

    :param file_path: the absolute path of the file to load 
    :return: a matrix representing a sudoku board 
    """
    board_list = []
    try:
        file = open(file_path, 'r')
        board_one_line = file.read()
        # convert each character to integer representation
        for n in board_one_line:
            if not n.isdigit():
                n = 0
            board_list.append(n)
        file.close()
    except FileNotFoundError as e:
        print(e)

    return board_list

from src.sudoku import Board
from src.ui import SudokuUI


board = Board()  # initialize board object
ui = SudokuUI(board)  # initialize ui
ui.mainloop()  # start ui
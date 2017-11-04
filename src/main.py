from src.sudoku import Board
from src.ui import SudokuUI


board = Board()
ui = SudokuUI(board)
ui.mainloop()

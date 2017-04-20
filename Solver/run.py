from Solver.SudokuBoard import SudokuBoard
from Solver.GUI import GUI
from tkinter import Tk
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

board = SudokuBoard() # New SudokuBoard object
parent = Tk()   # New TKinter window
GUI(parent, board) # New GUI with the Tkinter window and board
parent.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
parent.mainloop()   # Start the GUI
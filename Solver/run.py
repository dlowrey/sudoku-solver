from Solver import GUI, Board
from tkinter import Tk
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board

board = Board.Board()
parent = Tk()
GUI.GUI(parent, board)
parent.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
parent.mainloop()
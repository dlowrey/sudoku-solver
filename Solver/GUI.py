from tkinter import *
import time
MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class GUI(Frame):
    def __init__(self, parent, board):
        self.parent = parent

        # Set up
        Frame.__init__(self, parent)

        self.row = 0
        self.col = 0
        self.board = board
        self._initUI()

    def _initUI(self):

        self.parent.title("Sudoku Solver")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        clear_button = Button(self,
                              font="Arial",
                              text="Clear",
                              command=self.clear)
        clear_button.pack(side=LEFT)

        solve_button = Button(self,
                              font="Arial",
                              text="Solve",
                              command=self.solve)
        solve_button.pack(side=RIGHT)

        load_button = Button(self,
                             font="Arial",
                             text="Load Board",
                             command=self.load_board)
        load_button.pack(side=LEFT)

        save_button = Button(self,
                             font="Arial",
                             text="Save Board",
                             command=self.save_board)
        save_button.pack(side=LEFT)

        self.draw_grid()
        self.draw_puzzle()

        self.canvas.bind("<Button-1>", self.cell_clicked)
        self.canvas.bind("<Key>", self.key_pressed)

    def load_board(self):
        self.board.load_from_file()
        self.draw_puzzle()

    def save_board(self):
        self.board.save_to_file()

    def clear(self):
        self.board.clear_board()
        self.draw_puzzle()
        pass

    def solve(self):
        start = time.time()
        solved = self.board.solve()
        end = time.time()
        if solved:
            self.parent.title("Sudoku Solver - Puzzle solved in {0:.5g} seconds".format(end-start))
            self.draw_puzzle()
        else:
            self.parent.title("Sudoku Solver - PUZZLE INVALID OR UNSOLVABLE")

    def draw_grid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"
            line_width = 3 if i % 3 == 0 else 0
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=line_width)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=line_width)

    def draw_puzzle(self):
        self.canvas.delete("numbers")
        for r in range(9):
            for c in range(9):
                # Get number from actual game board here
                number = self.board.get_cell(r, c).get_number()
                if number != 0:
                    x = MARGIN + c * SIDE + SIDE / 2
                    y = MARGIN + r * SIDE + SIDE / 2
                    self.canvas.create_text(
                        x, y, text=number, tags="numbers"
                    )

    def cell_clicked(self, event):
        x = event.x
        y = event.y
        if MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
            self.canvas.focus_set()

            row = (y - MARGIN) // SIDE
            col = (x - MARGIN) // SIDE

            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            # else set self.row\col to the position we clicked
            else:
                self.row, self.col = row, col
        # draw a box using the coordinates we set from click
        self.draw_cursor()

    def draw_cursor(self):
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = MARGIN + self.col * SIDE + 1
            y0 = MARGIN + self.row * SIDE + 1
            x1 = MARGIN + (self.col + 1) * SIDE - 1
            y1 = MARGIN + (self.row + 1) * SIDE - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="red", tags="cursor"
            )

    def key_pressed(self, event):
        if self.row >= 0 and self.col >=0:
            if event.keysym == "Up" and self.row > 0:
                self.row -= 1
            if event.keysym == "Down" and self.row < 8:
                self.row += 1
            if event.keysym == "Right" and self.col < 8:
                self.col +=1
            if event.keysym == "Left" and self.col > 0:
                self.col -= 1
            if event.char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.board.get_cell(self.row, self.col).set_number(int(event.char))
                if self.col < 8:
                    self.col +=1
                elif self.row < 8:
                    self.col = 0
                    self.row += 1
                else:
                    self.col = 0
                    self.row = 0
            if event.keysym in ["Delete", "BackSpace"]:
                self.board.get_cell(self.row, self.col).reset_cell()

        self.draw_puzzle()
        self.draw_cursor()


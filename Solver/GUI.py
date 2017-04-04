from tkinter import Canvas, Frame, Button, BOTH, TOP, LEFT, RIGHT, Text, INSERT
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

        self.parent.title("Sudoku Solver - Copy a 9x9 Sudoku Puzzle and press 'Solve'")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              font="Arial",
                              text="Clear",
                              command=self._clear)
        clear_button.pack(side=LEFT, padx=20, pady=10)

        solve_button = Button(self,
                              font="Arial",
                              text="Solve",
                              command=self._solve)
        solve_button.pack(side=RIGHT, padx=20, pady=10)

        self._draw_grid()
        self._draw_puzzle()

        self.canvas.bind("<Button-1>", self._cell_clicked)
        self.canvas.bind("<Key>", self._key_pressed)

    def _clear(self):
        self.board._clear()
        self._draw_puzzle()
        pass

    def _solve(self):
        start = time.time()
        solved = self.board.solve()
        end = time.time()
        if solved:
            self._draw_puzzle()
        else:
            print("Unsolvable")
        print(end - start)

    def _draw_grid(self):
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

    def _draw_puzzle(self):
        self.canvas.delete("numbers")
        for r in range(9):
            for c in range(9):
                # Get number from actual game board here
                number = self.board._get_number(r, c)
                if number != 0:
                    x = MARGIN + c * SIDE + SIDE / 2
                    y = MARGIN + r * SIDE + SIDE / 2
                    self.canvas.create_text(
                        x, y, text=number, tags="numbers"
                    )

    def _cell_clicked(self, event):
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
        self._draw_cursor()

    def _draw_cursor(self):
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

    def _key_pressed(self, event):
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
                self.board.set_number(int(event.char), self.row, self.col)
                if self.col < 8:
                    self.col +=1
                elif self.row < 8:
                    self.col = 0
                    self.row += 1
                else:
                    self.col = 0
                    self.row = 0
            if event.keysym in ["Delete", "BackSpace"]:
                self.board.set_number(0, self.row, self.col)

        self._draw_puzzle()
        self._draw_cursor()


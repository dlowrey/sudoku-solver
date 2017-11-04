from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board


class SudokuUI(Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, board):
        """Initialize Tk frame"""
        self.sudoku = board
        self.parent = Tk()
        Frame.__init__(self, self.parent)

        self.row, self.col = -1, -1

        self.__initialize()

    def __initialize(self):
        """Set up all widgets on board"""
        self.parent.title("Sudoku Solver")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self,
                             width=WIDTH,
                             height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        clear_button = Button(self,
                              text="Clear",
                              command=self.__clear)
        clear_button.pack(fill=BOTH, side=BOTTOM)
        solve_button = Button(self,
                              text="Solve",
                              command=self.__solve)
        solve_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.__draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)

    def __draw_grid(self):
        """
        Draws grid divided with blue lines into 3x3 squares
        """
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        """Fill in the existing puzzle details"""
        self.canvas.delete("result")  # remove time stamp from view
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                cell = self.sudoku.board[i][j]
                number = cell.number
                if number != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    self.canvas.create_text(
                        x, y, text=number, tags="numbers", fill="black"
                    )

    def __draw_cursor(self):
        """Draw a red border around a selected cell"""
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

    def __draw_result(self, success, time):
        # create a oval (which will be a circle)
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(
            x0, y0, x1, y1,
            tags="result", fill="dark gray", outline="black"
        )
        # create text
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        text = "{0:.4f}s".format(time) if success else "Invalid Board"
        self.canvas.create_text(
            x, y,
            text=text, tags="result",
            fill="white", font=("Arial", 28)
        )

    def __cell_clicked(self, event):
        self.canvas.delete("result")  # remove time stamp from view
        x, y = event.x, event.y
        if MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN:
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = (y - MARGIN) // SIDE, (x - MARGIN) // SIDE

            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            else:
                self.row, self.col = row, col
        else:
            self.row, self.col = -1, -1

        self.__draw_cursor()

    def __key_pressed(self, event):
        """Catch all key press events and handle them"""
        if self.row >= 0 and self.col >= 0:
            if event.keysym in ["Up", "w"]:
                self.row = abs(((self.row + 8) % 9))
            elif event.keysym in ["Down", "Return", "s"]:
                self.row = abs(((self.row + 10) % 9))
            elif event.keysym in ["Right", "d"]:
                self.col = abs(((self.col + 10) % 9))
            elif event.keysym in ["Left", "a"]:
                self.col = abs(((self.col + 8) % 9))
            elif event.keysym in ["Delete", "BackSpace"]:
                self.sudoku.board[self.row][self.col].reset()
            elif event.char != "" and event.char in "1234567890":
                self.sudoku.board[self.row][self.col].number = int(event.char)
                self.__go_next()
            else:
                print("Unsupported key: \"{}\"".format(event.keysym))

            self.__draw_puzzle()
            self.__draw_cursor()

    def __go_next(self):
        """Advance to the next cell"""
        row = self.row
        col = self.col
        if col < 8:
            self.col += 1
        elif row < 8:
            self.row += 1
            self.col = 0
        else:
            self.row = 0
            self.col = 0

    def __clear(self):
        self.sudoku.clear()
        self.__draw_puzzle()

    def __solve(self):
        success, time = self.sudoku.solve()
        self.__draw_puzzle()
        self.__draw_result(success, time)
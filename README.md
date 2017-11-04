# SudokuSolver
A 9x9 Sudoku Puzzle solver using Python 3 and Tkinter
User Interface based off of [NewCoder Tutorial](http://newcoder.io/gui/part-3/)

## To Run ##
1. Download Python 3
2. Clone this repository
3. Run `src/main.py`


## Algorithm ##

The algorithm used is a simple brute force backtracking algorithm. Its
pseudo code is shown below.

````Python
    attempted = []
    for every cell in the board:
        if the cell does not have a number:

            calculate all possible non-tried numbers for that cell

            if the cell has possible numbers:
                try a new number in the cell
                put the cell in a list of attempted cells

            else if there are cells in attempted:
                reset this cell
                get the previous cell off of the end of attempted
                set the previous cell's number to 0
                reset the loop to the previous cell (backtrack)

            else the board is unsolvable

````


## Examples ##

### Initial Board ##

![Initial empty Sudoku Board](/assets/ex_blank.png)

### Filled in Sudoku Puzzle ###

Enter a valid Sudoku Puzzle by using the number pad and arrow keys, awsd, or
mouse to select cells.

![Initial empty Sudoku Board](/assets/ex_initial.png)

### Solved Puzzle ###

After entering a valid Sudoku puzzle, clicking the *Solve* button will
run the brute-force algorithm to solve it. If the board is invalid, the time
will be replaced with "Invalid Board".

![Initial empty Sudoku Board](/assets/ex_solved.png)

### Hide Time ###

To view the entire solved board, hide the time text by clicking anywhere on the
board or pressing any keys.

![Initial empty Sudoku Board](/assets/ex_solved_board.png)

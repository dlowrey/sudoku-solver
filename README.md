# Sudoku Solver
A 9x9 Sudoku Puzzle solver using Python 3 and Tkinter
User Interface based off of [NewCoder Tutorial](http://newcoder.io/gui/part-3/)
Other branch `simple` exist for different reasons but are the same project.
- `simple` is the project without the more *pythonic* stuff in it.

## To Run ##
1. Download Python 3
2. Clone this repository
3. Navigate to `SudokuSolver/`
4. Run `python main.py`


## Algorithm ##

[Backtracking](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Backtracking)

The algorithm used is a brute force backtracking algorithm with a time complexity of O(n<sup>m</sup>) where *n* is 
the number of possibilities for each cell and *m* is the number of blank cells. Its
pseudo code is shown below.

````Text
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

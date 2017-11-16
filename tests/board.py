from src.sudoku import Board, Cell

# Test creation of board object
board = Board()
passed = type(board) == Board
print("create Board object success: {}".format(passed))

# Test that the board has cell objects
passed = True
for r in range(9):
    for c in range(9):
        cell = board.board[r][c]
        passed = passed and type(cell) == Cell
print("board made of Cell objects: {}".format(passed))

# Test the boards validation method
valid = board.is_valid()
passed = valid
print("validate empty board success: {}".format(passed))

# Make the board invalid and test validation method
cell_1 = board.board[0][0]
cell_1.number = 1
cell_2 = board.board[0][1]
cell_2.number = 1
valid = board.is_valid()
passed = not valid
print("validate invalid board success: {}".format(passed))

# Test clearing the board
board.clear()
passed = True
for r in range(9):
    for c in range(9):
        if board.board[r][c].number != 0:
            passed = False
print("reset the entire board success: {}".format(passed))

# Test printing out the board
print(str(board))


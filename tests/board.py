from src.sudoku import Board, Cell

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

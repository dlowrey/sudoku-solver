from src.Sudoku import Board

board = Board()
print(str(board))

board.solve()

print(str(board))
print(board.is_valid())

from src.sudoku import Cell

# Test creating cell
my_cell = Cell(1, 2)
passed = type(my_cell) == Cell
print("create Cell object success: {}".format(passed))

# Test setting possible numbers
possible = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_cell.set_possible_numbers({1, 2, 3, 4, 5, 6, 7, 8, 9})
passed = my_cell.possible_numbers == possible
print("set possible numbers success: {}".format(passed))

# Test trying new number
my_cell.try_new_number()
passed = my_cell.number != 0
print("try_new_number success: {}".format(passed))

# Test reset number to 0
my_cell.reset_number()
passed = my_cell.number == 0
print("reset number success: {}".format(passed))

# Test exhaustion flag
while my_cell.exhausted:
    my_cell.try_new_number()
passed = not my_cell.exhausted
print("cell exhaustion success: {}".format(passed))

# Test complete reset of cell (except position)
my_cell.reset()
passed = not my_cell.number and not my_cell.possible_numbers and not my_cell.exhausted


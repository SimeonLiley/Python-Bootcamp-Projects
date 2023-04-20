# Minesweeper programme that solves a 2D list of - and # as per the rules of minesweeper.
# # are bombs and - are safe spaces

def check_mine(row_index, col_index):
    """
    check_mine checks for mines (# symbols) in agacent 2D list elements based on row and column index
    Args:
        row_index: The given row index of the starting location
        col_index: The column index of the starting location
    Returns:
        mine_count: the total number of ajacent mines
    """
    mine_count = 0
    # if a middle square checks all 8 sorrounding values for mines #
    if row_index > 0 and row_index < rows-1 and col_index > 0 and col_index < columns-1:
        if mine_gird[row_index-1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index+1] == "#":
            mine_count += 1       
        return mine_count

    # check if top left corner
    if row_index == 0 and col_index == 0:
        if mine_gird[row_index][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index+1] == "#":
            mine_count += 1
        return mine_count
    # check if top right corner
    if row_index == 0 and col_index == columns-1:
        if mine_gird[row_index][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index] == "#":
            mine_count += 1
        return mine_count
    # check if bottom left corner
    if row_index == rows-1 and col_index == 0:
        if mine_gird[row_index][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index+1] == "#":
            mine_count += 1
        return mine_count
    # check if bottom right corner
    if row_index == rows-1 and col_index == columns-1:
        if mine_gird[row_index][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index] == "#":
            mine_count += 1
        return mine_count
    
    # check if top row (not corner)
    if row_index == 0 and col_index > 0 and col_index < columns-1:
        if mine_gird[row_index][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index+1] == "#":
            mine_count += 1
        return mine_count
    # check if bottom row (not corner)
    if row_index == rows-1 and col_index > 0 and col_index < columns-1:
        if mine_gird[row_index][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index+1] == "#":
            mine_count += 1
        return mine_count
    # check if left column (not corner)
    if row_index > 0 and row_index < rows-1 and col_index == 0:
        if mine_gird[row_index-1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index][col_index+1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index+1] == "#":
            mine_count += 1
        return mine_count
    # check if right column (not corner)
    if row_index > 0 and row_index < rows-1 and col_index == columns-1:
        if mine_gird[row_index-1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index-1][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index][col_index-1] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index] == "#":
            mine_count += 1
        if mine_gird[row_index+1][col_index-1] == "#":
            mine_count += 1
        return mine_count
    else:
        return 0

# Another example of a grid
"""
mine_gird = [['-', '#', '-', '#'],
            ['-', '-', '-', '#'],
            ['#', '#', '-', '-'],
            ['-', '#', '-', '-'],
            ['-', '-', '#', '-']]
"""
# Starting mine grid
mine_gird = [['-', '-', '-', '#', '#'],
            ['-', '#', '-', '-', '-'],
            ['-', '-', '#', '-', '-'],
            ['-', '#', '#', '-', '-'],
            ['-', '-', '-', '-', '-']]

# Print strating grid
for row_index, row_element in enumerate(mine_gird):
    print("\n", end="")
    for col in row_element:
        print(col, end=".")

# Varoables for itteration 
rows = len(mine_gird)
columns = len(mine_gird[0])
mine_count = 0

# Iterate through grid changing - to number of agacent #s using mine_count function if a - is found
for row_index, row_element in enumerate(mine_gird):
    for col_index, col_element in enumerate(row_element):
        if mine_gird[row_index][col_index] == "-":
            mine_count = check_mine(row_index, col_index)
            mine_gird[row_index][col_index] = mine_count

# Print output mine grid
print()
for row_index, row_element in enumerate(mine_gird):
    print("\n", end="")
    for col in row_element:
        print(col, end=".")
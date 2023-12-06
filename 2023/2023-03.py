from load_data import get_data
import numpy as np
import re

data = get_data(day='3', as_list=True)


# Part 1
field = np.mat([[i for i in row] for row in data])
rows, cols = field.shape

field_cover = np.zeros(shape=(rows,cols), dtype=int)

symbols = re.sub('[.0-9]','',''.join(data))

def add_point(matrix: np.mat, row: int, col: int) -> np.mat:
    """Add point and ensure in range of matrix"""
    row_len, col_len = matrix.shape
    if 0 <= row and row < row_len and 0 <= col and col < col_len:
        matrix[row, col] = 1
    return matrix


def add_circle_points(matrix: np.mat, center_row: int, center_col) -> np.mat:
    for i in range(-1,2):
        for j in range(-1,2):
            matrix = add_point(matrix, center_row+i, center_col+j)
    return matrix


for row in range(rows):
    for col in range(cols):
        if field[row, col] in symbols:
            field_cover = add_circle_points(field_cover, row, col)

numbers = []
for row in range(rows):
    col = 0
    while col < cols:
        if field_cover[row, col] == 1 and field[row, col].isdigit():
            while col-1 >= 0 and field[row, col-1].isdigit():
                col -= 1
            digits = field[row, col]
            while col+1 < cols and field[row, col+1].isdigit():
                col += 1
                digits += field[row, col]
            numbers.append(int(digits))

        col += 1

print(sum(numbers))


# Part 2
field = np.mat([[i for i in row] for row in data])
rows, cols = field.shape

gear_dict = {}
field_cover = np.zeros(shape=(rows,cols), dtype=int)
for row in range(rows):
    for col in range(cols):
        if field[row, col] == '*':
            gear_dict[(row, col)] = []
            field_cover = add_circle_points(field_cover, row, col)


def get_gear_spot(gear_dict: dict, row: int, col: int) -> (int,int):
    """Find the gear spot based on identified adjacent point."""
    for i in range(-1,2):
        for j in range(-1,2):
            if (row+i,col+j) in gear_dict.keys():
                return (row+i,col+j)


# Find all numbers adjecent to gear symbol.
for row in range(rows):
    col = 0
    while col < cols:
        if field_cover[row, col] == 1 and field[row, col].isdigit():
            
            gear_found = get_gear_spot(gear_dict, row, col)           

            while col-1 >= 0 and field[row, col-1].isdigit():
                col -= 1
            digits = field[row, col]
            while col+1 < cols and field[row, col+1].isdigit():
                col += 1
                digits += field[row, col]
            
            gear_dict[gear_found] = gear_dict[gear_found] + [(int(digits))]
        col += 1


# Compute gear ratio where two numbers adjecent to gear. 
gear_ratios = [l[0] * l[1] for l in gear_dict.values() if len(l) == 2]
print(sum(gear_ratios))

# BOJ Coding Test Practice
# 17406: 배열 돌리기 4
#
#     https://www.acmicpc.net/problem/17406
#
# ==============================================================================

from copy import deepcopy
from itertools import permutations

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def get_matrix_value(matrix):
    sums = list(map(sum, matrix))
    return min(sums)


def rotate_clockwise(matrix, row, col, diff):
    for d in range(1, diff+1):
        have_to_change = (2*d + 1)**2 - (2*d - 1)**2
        current_row, current_col = row - d - 1, col - d - 1
        current_value = matrix[current_row][current_col]
        row_lower_bound = row - d - 1
        row_upper_bound = row + d - 1
        col_lower_bound = col - d - 1
        col_upper_bound = col + d - 1
        row_direction, col_direction = directions[0]
        direction_index = 1
        for _ in range(have_to_change):
            next_row = current_row + row_direction
            next_col = current_col + col_direction
            bound_beyond = next_row < row_lower_bound or next_row > row_upper_bound or next_col < col_lower_bound or next_col > col_upper_bound
            if bound_beyond:
                row_direction, col_direction = directions[direction_index]
                direction_index += 1
                next_row = current_row + row_direction
                next_col = current_col + col_direction
            next_value = matrix[next_row][next_col]
            matrix[next_row][next_col] = current_value
            current_value = next_value
            current_row = next_row
            current_col = next_col


def rotate_matrix(matrix, rotations):
    result = deepcopy(matrix)
    for rotation in rotations:
        row, col, diff = rotation
        rotate_clockwise(result, row, col, diff)
    return result


matrix = []
rotations = []
values = []
rows, cols, rotation = list(map(int, input().split()))
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(rotation):
    r = list(map(int, input().split()))
    rotations.append(r)

for rotations_p in permutations(rotations, len(rotations)):
    rotated_matrix = rotate_matrix(matrix, rotations_p)
    value = get_matrix_value(rotated_matrix)
    values.append(value)


print(min(values))

import pytest


def solve_puzzle_1(array):
    sum = 0
    for val in array:
        if val[1] != 'N':
            sum += val[0]
    return sum


def solve_puzzle_2(array):
    sum = 0
    prev_gears = {}

    for val in array:
        if val[1] == '*':
            valstring = str(val[2])
            if valstring in prev_gears:
                sum += val[0] * prev_gears[valstring]

            prev_gears[valstring] = val[0]

    return sum


def symbol(char):
    if char.isnumeric() or char == '.':
        return False
    return True


def extract_numbers_and_symbols(text):
    arr = []
    modified = text.splitlines()
    # add an empty row as first and last, and skip handling those, this way we can always check for symbols on top or below
    modified.insert(0, ['.']*len(modified[0]))
    modified.append(['.']*len(modified[0]))
    for idy, line in enumerate(modified):
        if idy == 0 or idy == len(modified) - 1:
            continue
        number = ''
        adjacent = 'N'
        adjacent_pos = [0, 0]
        for idx, val in enumerate(line):
            if val.isnumeric():
                number += val
                # check adjacency

                # up
                if symbol(modified[idy-1][idx]):
                    adjacent = modified[idy-1][idx]
                    adjacent_pos = [idy-1, idx]

                # down
                if symbol(modified[idy+1][idx]):
                    adjacent = modified[idy+1][idx]
                    adjacent_pos = [idy+1, idx]

                if idx > 0:
                    # left
                    if symbol(modified[idy][idx-1]):
                        adjacent = modified[idy][idx-1]
                        adjacent_pos = [idy, idx-1]
                    # upper left
                    if symbol(modified[idy-1][idx-1]):
                        adjacent = modified[idy-1][idx-1]
                        adjacent_pos = [idy-1, idx-1]
                    # down left
                    if symbol(modified[idy+1][idx-1]):
                        adjacent = modified[idy+1][idx-1]
                        adjacent_pos = [idy+1, idx-1]

                # if last char on line, dont check right, and store number
                if idx + 1 < len(line):
                    # right
                    if symbol(modified[idy][idx+1]):
                        adjacent = modified[idy][idx+1]
                        adjacent_pos = [idy, idx+1]
                    # upper right
                    if symbol(modified[idy-1][idx+1]):
                        adjacent = modified[idy-1][idx+1]
                        adjacent_pos = [idy-1, idx+1]
                    # down right
                    if symbol(modified[idy+1][idx+1]):
                        adjacent = modified[idy+1][idx+1]
                        adjacent_pos = [idy+1, idx+1]
                else:
                    arr.append([int(number), adjacent, adjacent_pos])

            else:
                if len(number) > 0:
                    arr.append([int(number), adjacent, adjacent_pos])
                number = ''
                adjacent = 'N'
                adjacent_pos = [0, 0]

    return arr


two_d_data = """.+.23*......
1........+44"""

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def test_extract_numbers_and_symbols():
    assert extract_numbers_and_symbols(
        '1.23*22') == [[1, 'N', [0, 0]], [23, '*', [1, 4]], [22, '*', [1, 4]]]
    assert extract_numbers_and_symbols(two_d_data) == [
        [23, '*', [1, 5]], [1, '+', [1, 1]], [44, '+', [2, 9]]]


def test_solve_puzzles(day3_input):
    assert solve_puzzle_1(
        [[1, 'N', [0, 0]], [23, '*', [1, 4]], [22, '*', [1, 4]]]) == 45
    assert solve_puzzle_2([[1, 'N', [0, 0]], [
                          23, '*', [1, 4]], [1, 'N', [0, 0]], [22, '*', [1, 4]], [22, '*', [1, 5]]]) == 506

    assert solve_puzzle_1(extract_numbers_and_symbols(example)) == 4361
    assert solve_puzzle_1(extract_numbers_and_symbols(day3_input)) == 559667

    assert solve_puzzle_2(extract_numbers_and_symbols(example)) == 467835
    assert solve_puzzle_2(extract_numbers_and_symbols(
        day3_input)) == 86841457  # 87223437

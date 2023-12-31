def solve_puzzle_1(input):
    all_grids = [r.strip() for r in input.split('\n\n')]
    total = 0

    for val in all_grids:
        row = mirror_in_grid(val, 'row')
        if row > 0:
            total += row * 100
        else:
            col = mirror_in_grid(val, 'col')
            if col > 0:
                total += col
            else:
                raise Exception('No mirror found')
    
    return total

def mirror_in_grid(grid, type):
    grid = grid.splitlines()
    grid = [list(x) for x in grid]

    if type == 'col':
        grid = list(zip(*grid))

    for i in range(len(grid)):
        mirror = False
        j = i
        k = i + 1
        while j >= 0 and k < len(grid):
            if is_mirror(grid[j],grid[k]):
                j -= 1
                k += 1
                mirror = True
            else:
                mirror = False
                break
        if mirror:
            return i+1
    
    return -1

def is_mirror(input1, input2):
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            return False
    return True

def test_is_mirror():
    input1 = '##......#'
    input2 = '#..#....#'
    
    assert is_mirror(input1,input1) == True
    assert is_mirror(input1,input2) == False

input_example_row = """#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

input_example_col = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#."""

def test_mirror_in_grid():
    input_row = '#.##..##.\n#.##..##.'

    input_row_2 = '##.#\n..##'

    assert mirror_in_grid(input_row, 'row') == 1
    assert mirror_in_grid(input_example_row, 'row') == 4
    assert mirror_in_grid(input_row_2, 'row') == -1
    assert mirror_in_grid(input_example_col, 'col') == 5

def test_solve_puzzle_1(day13_input):
    assert solve_puzzle_1(input_example_row + '\n\n' + input_example_col) == 405
    assert solve_puzzle_1(day13_input) == 32371



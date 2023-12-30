example_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

def galaxy_distances(input):
    galaxy_map = create_map(input)
    galaxies = []

    for idx_y, y in enumerate(galaxy_map):
        for idx_x, x in enumerate(y):
            if x == '#':
                galaxies.append([idx_x, idx_y])
    
    distance_sum = 0
    
    for idx_1, val in enumerate(galaxies):
        for idx_2 in range(idx_1+1, len(galaxies), 1):
            distance_sum += measure_distance(val, galaxies[idx_2])

    return distance_sum

def create_map(input):
    first = input.splitlines()
    second = [ list(x) for x in first ]
    third = expand_rows(second)
    fourth = expand_columns(third)

    return fourth

def expand_rows(input_list):
    new_list = []
    for val in input_list:
        if '#' not in val:
            new_list.append(val)
        new_list.append(val)

    return new_list

def expand_columns(input_list):
    new_list = [ [] for _ in range(len(input_list)) ]
    for x in range(len(input_list[0])):
        empty = True
        for y in range(len(input_list)):
            new_list[y].append(input_list[y][x])
            if input_list[y][x] == '#':
                empty = False
        
        if empty:
            new_list = add_column(new_list, len(new_list), '.')
    
    return new_list

def add_column(input_list, column, filler):
    new_list = input_list
    for i in range(len(input_list)):
        new_list[i].insert(column, filler)
    return new_list

def measure_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def test_add_column():
    twodlist = [['a', 'b', 'c'],['d', 'e', 'f']]
    
    new_list = add_column(twodlist, 2, 'n')

    assert new_list[0][2] == 'n'
    assert new_list[0][3] == 'c'
    assert len(new_list) == 2

def test_expand_rows():
    twodlist = [['.', '.','#','.'],['.', '.', '.', '.'],['#', '.', '.', '.']]

    expanded = expand_rows(twodlist)
    assert len(expanded) == 4
    assert expanded[1][3] == '.'
    assert expanded[2][3] == '.'

def test_expand_columns():
    twodlist = [['.', '.','#','.'],['.', '.', '.', '.'],['#', '.', '.', '.']]

    expanded = expand_columns(twodlist)
    assert len(expanded) == 3
    assert len(expanded[0]) == 6
    assert expanded[1][3] == '.'
    assert expanded[2][5] == '.'

def test_create_map():
    input = "....\n#..#\n.#.#\n"
    map = create_map(input)
    assert len(map) == 4
    assert len(map[0]) == 5

def test_measure_distance():
    p1 = [2,2]
    p2 = [3,3]
    p3 = [1,1]

    assert measure_distance(p1, p2) == 2
    assert measure_distance(p1, p3) == 2

def test_galaxy_distances(day11_input):
    input = "....\n#..#\n.#.#\n"
    assert galaxy_distances(input) == 19
    assert galaxy_distances(example_input) == 374
    assert galaxy_distances(day11_input) == 9805264
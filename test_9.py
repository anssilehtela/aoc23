

example_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def solve_puzzle_1(input):
    total = 0
    for val in input.splitlines():
        total += next_val_in_seq([int(v) for v in val.split()])

    return total


def solve_puzzle_2(input):
    total = 0
    for val in input.splitlines():
        total += previous_val_in_seq([int(v) for v in val.split()])

    return total


def test_solve_puzzle_1(day9_input):
    assert solve_puzzle_1(example_input) == 114
    assert solve_puzzle_1(day9_input) == 1637452029


def test_solve_puzzle_2(day9_input):
    assert solve_puzzle_2(example_input) == 2
    assert solve_puzzle_2(day9_input) == 908


def next_val_in_seq(seq):
    complete = create_complete(seq)

    for idx in range(len(complete)):
        if idx == 0:
            complete[idx].append(0)
        else:
            complete[idx].append(complete[idx][-1] + complete[idx-1][-1])

    return complete[-1][-1]


def previous_val_in_seq(seq):
    complete = create_complete(seq)

    for idx in range(len(complete)):
        if idx == 0:
            complete[idx].insert(0, 0)
        else:
            complete[idx].insert(0, complete[idx][0] - complete[idx-1][0])

    return complete[-1][0]


def test_next_val_in_seq():
    assert next_val_in_seq([0, 3, 6, 9, 12, 15]) == 18


def test_previous_val_in_seq():
    assert previous_val_in_seq([10, 13, 16, 21, 30, 45]) == 5


def create_complete(seq):
    complete = [seq]
    x = 0
    while True:
        new_list = []
        complete[x].reverse()
        for i in range(len(complete[x]) - 1):
            new_list.append(complete[x][i] - complete[x][i + 1])
        complete[x].reverse()
        new_list.reverse()
        complete.append(new_list)
        if all(v == 0 for v in new_list):
            break
        x += 1
    complete.reverse()
    return complete



example = """Time:      7  15   30
Distance:  9  40  200"""


def solve_puzzle(input):
    races = parse_input(input)
    sum = 1

    for val in races:
        wins = win_conditions(val[0], val[1])
        sum *= len(wins)

    return sum


def win_conditions(time, record):
    wins = []
    for ms_held in range(time+1):
        if ms_held*(time-ms_held) > record:
            wins.append(ms_held)
    return wins


def parse_input(text):
    lines = text.splitlines()
    times = [int(l) for l in lines[0][6:].split()]
    distances = [int(d) for d in lines[1][9:].split()]
    races = []

    for i in range(len(times)):
        races.append([times[i], distances[i]])
    return races


def test_solve_puzzle(day6_input):
    assert solve_puzzle(example) == 288
    assert solve_puzzle(day6_input) == 440000

    # this actually solves puzzle part 2, skipped parsing the input by code as it was so easy
    assert len(win_conditions(42686985, 284100511221341)) == 26187338


def test_win_conditions():
    assert win_conditions(3, 1) == [1, 2]
    assert len(win_conditions(71530, 940200)) == 71503


def test_parse_input():
    assert parse_input(example) == [[7, 9], [15, 40], [30, 200]]

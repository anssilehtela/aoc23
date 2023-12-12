

example_input = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

example_input_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

example_input_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

def parse_input(input):
    lines = input.splitlines()
    command = list(lines[0])
    dicti = {}
    starting_nodes = []

    for val in lines[2:]:
        dicti[val[:3]] = [val[7:10],val[12:15]]
        if val[2:3] == 'A':
            starting_nodes.append(val[:3])

    return command, dicti, starting_nodes

def test_parse_input():
    command, output, starting_nodes = parse_input(example_input)

    assert command == ['R', 'L']
    assert len(output) == 7
    assert output['AAA'] == ['BBB', 'CCC']
    assert len(starting_nodes) == 1
    assert starting_nodes[0] == 'AAA'

    command, output, starting_nodes = parse_input(example_input_3)
    assert starting_nodes == ['11A', '22A']


def solve_puzzle(example_input):
    command, dicti, starting_nodes = parse_input(example_input)

    i = 0
    count = 0
    next = 'AAA'
    while True:
        if command[i] == 'L':
            next = dicti[next][0]
        else:
            next = dicti[next][1]
        count +=1
        if next == 'ZZZ':
            break
        if i == len(command) - 1:
            i = 0
        else:
            i += 1

    return count

def solve_puzzle_2(example_input):
    command, dicti, starting_nodes = parse_input(example_input)

    
    i = 0
    count = 0
    ending = ['a'] * len(starting_nodes)
    while True:
        for idx, val in enumerate(starting_nodes):
            if command[i] == 'L':
                starting_nodes[idx] = dicti[val][0]
            else:
                starting_nodes[idx] = dicti[val][1]
            ending[idx] = starting_nodes[idx][2]
        
        count +=1
        if count % 1000000 == 0:
            print(count)
            print(ending)
        if all(x == 'Z' for (x) in ending):
            break
        else:
            ending = ['a'] * len(starting_nodes)
        if i == len(command) - 1:
            i = 0
        else:
            i += 1

    return count

def test_solve_puzzle(day8_input):
    assert solve_puzzle(example_input) == 2
    assert solve_puzzle(example_input_2) == 6
    assert solve_puzzle(day8_input) == 23147

def test_solve_puzzle_2(day8_input):
    assert solve_puzzle_2(example_input_3) == 6
    assert solve_puzzle_2(day8_input) == 23147
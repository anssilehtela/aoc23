import itertools


example_input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def condition_record(input):
    count = 0
    counts = []
    for val in input:
        if val == '#':
            count += 1
        else:
            if count > 0:
                counts.append(count)
                count = 0
    if count > 0:
        counts.append(count)
    
    return counts

def test_condition_record():
    input = '.#.#..###'

    assert condition_record(input) == [1,1,3]

def create_variations(input):
    variations = []
    q = input.count('?')
    for item in itertools.product(['.','#'], repeat = q):
        new = input
        for val in item:
            new = new.replace('?', val, 1)
        variations.append(new)
    
    return variations


def test_create_variations():
    input = '???.###'

    variations = create_variations(input)

    assert len(variations) == 8
    assert '###.###' in variations

def condition_variations(input):
    condition_records_input, contiguous_group_input = input.split(' ')
    contiguous_group_input = [int(x) for x in contiguous_group_input.split(',')]

    variations = create_variations(condition_records_input)
    condition_records = []
    for val in variations:
        condition_records.append(condition_record(val))

    return condition_records.count(contiguous_group_input)


def test_condition_variations():
    input = '???.### 1,1,3'
    input2 = '.??..??...?##. 1,1,3'

    assert condition_variations(input) == 1
    assert condition_variations(input2) == 4

def solve_puzzle_1(input):
    lines = input.splitlines()
    sum = 0
    for line in lines:
        sum += condition_variations(line)

    return sum

def test_solve_puzzle_1(day12_input):
    assert solve_puzzle_1(example_input) == 21
    assert solve_puzzle_1(day12_input) == 7191
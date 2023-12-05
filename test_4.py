import time
import pytest


def win_condition_1(winners, numbers):
    points = 0
    for num in numbers:
        if num in winners:
            if points == 0:
                points += 1
            else:
                points *= 2
    return points


def win_condition_2(winners, numbers):
    points = 0
    for num in numbers:
        if num in winners:
            points += 1

    return points


def parse_line(text):
    card_no = int(text[4:text.index(':')].strip())
    no_prefix = text[text.index(':')+1:]
    idx_of_delimiter = no_prefix.index('|')
    winners = no_prefix[:idx_of_delimiter].split()
    numbers = no_prefix[idx_of_delimiter+1:].split()

    return [card_no, winners, numbers]


def puzzle_1(input):
    sum = 0
    for line in input.splitlines():
        res = parse_line(line)
        sum += win_condition_1(res[1], res[2])

    return sum


def puzzle_2(input):
    scratch_dict = {}
    scratch_list = input.splitlines()
    for item in scratch_list:
        scratch_dict[item[4:item.index(':')].strip()] = item

    for idx, line in enumerate(scratch_list):
        res = parse_line(line)
        multiplier = win_condition_2(res[1], res[2])
        for i in range(multiplier):
            scratch_list.append(scratch_dict[str(res[0] + i + 1)])

    return len(scratch_list)


def test_parse_line():
    assert parse_line('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53') == [
        1, ['41', '48', '83', '86', '17'], ['83', '86', '6', '31', '17', '9', '48', '53']]


def test_win_condition_1():
    assert win_condition_1(['1'], ['1']) == 1
    assert win_condition_1(['1', '3', '7', '8'], ['1', '7', '8']) == 4
    assert win_condition_1(['1', '3', '7', '8'], ['11']) == 0


def test_win_condition_2():
    assert win_condition_2(['1'], ['1']) == 1
    assert win_condition_2(['1', '3', '7', '8'], ['1', '7', '8']) == 3
    assert win_condition_2(['1', '3', '7', '8'], ['11']) == 0


example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def test_puzzle_1(day4_input):
    assert puzzle_1(example) == 13
    assert puzzle_1(day4_input) == 25174


def test_puzzle_2(day4_input):
    assert puzzle_2(day4_input) == 6420979

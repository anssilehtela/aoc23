import pytest
import aoc23.data as data


def solve_puzzles(match):
    sum_1 = 0
    sum_2 = 0
    for idx, val in enumerate(match.splitlines()):
        game = Game()
        game.parse(val)
        if game.valid():
            sum_1 += idx + 1
        sum_2 += game.min_balls()

    return sum_1, sum_2


class Game:

    def __init__(self) -> None:
        self.sets = []

    def parse(self, text):
        for val in text[text.index(':')+1:].split(';'):
            self.sets.append(val)

    def valid(self):
        for val in self.sets:
            set = Set()
            set.parse(val)
            if not set.valid():
                return False
        return True

    def min_balls(self):
        min_red = 1
        min_green = 1
        min_blue = 1
        for val in self.sets:
            set = Set()
            set.parse(val)
            if set.balls['red'] > min_red:
                min_red = set.balls['red']
            if set.balls['green'] > min_green:
                min_green = set.balls['green']
            if set.balls['blue'] > min_blue:
                min_blue = set.balls['blue']

        return min_red * min_green * min_blue


class Set:
    max_red = 12
    max_green = 13
    max_blue = 14

    def __init__(self) -> None:
        self.balls = {}
        self.balls['red'] = 0
        self.balls['green'] = 0
        self.balls['blue'] = 0

    def parse(self, text):
        arr = [x.strip() for x in text.split(',')]
        for val in arr:
            ball = val.split()
            ball.reverse()
            self.balls[ball[0]] = int(ball[1])

    def valid(self):
        if self.balls['red'] > self.max_red or self.balls['green'] > self.max_green or self.balls['blue'] > self.max_blue:
            return False
        return True


def test_solve_puzzles():
    match = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    puzzle_match = data.day2

    valid_1, balls_1 = solve_puzzles(match)
    valid_2, balls_2 = solve_puzzles(puzzle_match)

    assert valid_1 == "FILTERED"
    assert balls_1 == "FILTERED"
    assert valid_2 == "FILTERED"
    assert balls_2 == "FILTERED"


def test_game():
    game1 = Game()
    game2 = Game()

    game1.parse("Game 1: 3 blue; 2 red; 4 green")
    game2.parse("Game 2: 1000 red, 2 blue")

    assert len(game1.sets) == 3
    assert len(game2.sets) == 1
    assert game1.sets[1] == ' 2 red'
    assert game2.sets[0] == ' 1000 red, 2 blue'
    assert game1.valid()
    assert game2.valid() == False

    assert game1.min_balls() == 24
    assert game2.min_balls() == 2000


def test_set():
    set1 = Set()
    set2 = Set()

    set1.balls['green'] = 3
    set2.balls['green'] = 300

    assert set1.balls['red'] == 0
    assert set1.balls['green'] == 3
    assert set1.balls['blue'] == 0
    assert set1.valid() == True
    assert set2.valid() == False


def test_parse_set():
    set = Set()
    set.parse(" 3 blue, 4 red")
    assert set.balls['red'] == 4
    assert set.balls['green'] == 0
    assert set.balls['blue'] == 3

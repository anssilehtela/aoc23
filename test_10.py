

class Metalfield:

    def __init__(self, raw_map):
        self.raw_map = raw_map
        self.map = self.parse_map()
        self.starting_pos = self.find_starting_pos()
        self.pos = self.starting_pos
        self.marker = self.deduct_staring_marker()
        self.previous_pos = None
        self.moves = []

    def parse_map(self):
        array = []
        for i, val in enumerate(self.raw_map.splitlines()):
            array.append([])
            for j, val in enumerate(val):
                array[i].append(val)
        return array
    
    def find_starting_pos(self):
        for idx, val in enumerate(self.map):
            if 'S' in val:
                return [idx, val.index('S')]
            
    def move(self):
        if len(self.moves) > 0 and self.pos == self.starting_pos:
                #finished
                return False
        
        next_pos = None
        if self.previous_pos == None:
            match self.marker:
                case '|':
                    next_pos = [self.pos[0]-1, self.pos[1]]
                case 'F':
                    next_pos = [self.pos[0], self.pos[1]+1]
                case '7':
                    next_pos = [self.pos[0], self.pos[1]-1]
                case '-':
                    next_pos = [self.pos[0], self.pos[1]+1]
                case 'J':
                    next_pos = [self.pos[0]-1, self.pos[1]]
                case 'L':
                    next_pos = [self.pos[0], self.pos[1]+1]
        elif self.previous_pos[0] > self.pos[0]: #coming from down
            match self.marker:
                case '|':
                    next_pos = [self.pos[0]-1, self.pos[1]]
                case 'F':
                    next_pos = [self.pos[0], self.pos[1]+1]
                case '7':
                    next_pos = [self.pos[0], self.pos[1]-1]
                case _:
                    raise Exception
        elif self.previous_pos[1] < self.pos[1]: #coming from left
            match self.marker:
                case '-':
                    next_pos = [self.pos[0], self.pos[1]+1]
                case '7':
                    next_pos = [self.pos[0]+1, self.pos[1]]
                case 'J':
                    next_pos = [self.pos[0]-1, self.pos[1]]
                case _:
                    raise Exception
        elif self.previous_pos[0] < self.pos[0]: #coming from up
            match self.marker:
                case '|':
                    next_pos = [self.pos[0]+1, self.pos[1]]
                case 'L':
                    next_pos = [self.pos[0], self.pos[1]+1]
                case 'J':
                    next_pos = [self.pos[0], self.pos[1]-1]
                case _:
                    raise Exception
        elif self.previous_pos[1] > self.pos[1]: #coming from right
            match self.marker:
                case '-':
                    next_pos = [self.pos[0], self.pos[1]-1]
                case 'L':
                    next_pos = [self.pos[0]-1, self.pos[1]]
                case 'F':
                    next_pos = [self.pos[0]+1, self.pos[1]]
                case _:
                    raise Exception
        else:
            raise Exception
        
        self.previous_pos = self.pos
        self.pos = next_pos
        self.moves.append(self.pos)
        self.marker = self.map[self.pos[0]][self.pos[1]]
        return True

    def deduct_staring_marker(self):
        possible = ['-','L','J','F', '7','|']
        if self.map[self.pos[0]-1][self.pos[1]] in ['-', 'L', 'J', '.']:
            possible.remove('|')
            possible.remove('L')
            possible.remove('J')
        if self.map[self.pos[0]][self.pos[1]+1] in ['|', 'L', 'F', '.']:
            if '-' in possible: possible.remove('-') 
            if 'L' in possible: possible.remove('L')
            if 'F' in possible: possible.remove('F')
        if self.map[self.pos[0]][self.pos[1]-1] in ['|', 'J', '7', '.']:
            if '-' in possible: possible.remove('-')
            if 'J' in possible: possible.remove('J')
            if '7' in possible: possible.remove('7')
        if self.map[self.pos[0]+1][self.pos[1]] in ['-', '7', 'F', '.']:
            if '|' in possible: possible.remove('|')
            if 'F' in possible: possible.remove('F')
            if '7' in possible: possible.remove('7')
        
        if len(possible) == 1:
            return possible[0]

        raise Exception

def solve_puzzle_1(input):
    metalfield = Metalfield(input)

    moving = True
    while moving:
        moving = metalfield.move()
    
    moves = len(metalfield.moves)

    if moves % 2 == 0:
        return moves / 2
    else:
        return (moves-1) / 2 + 1


raw_map = """.....
.S-7.
.|.|.
.L-J.
....."""

example_input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

def test_solve_puzzle_1(day10_input):
    assert solve_puzzle_1(example_input) == 8
    assert solve_puzzle_1(day10_input) == 7107


def test_metalfied():
    mf = Metalfield(raw_map)
    assert mf.map[1][2] == '-'
    assert mf.starting_pos == [1, 1]
    assert mf.pos == [1, 1]
    assert mf.previous_pos == None
    assert mf.marker == 'F'
    assert mf.moves == []

def test_move():
    mf = Metalfield(raw_map)
    assert mf.move() == True
    assert mf.move() == True
    assert mf.pos == [1, 3]
    assert mf.previous_pos == [1, 2]
    assert mf.marker == '7'
    assert len(mf.moves) == 2
    for i in range(6):
        assert mf.move() == True
    assert mf.move() == False
    assert len(mf.moves) == 8
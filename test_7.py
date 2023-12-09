example_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def solve_puzzle(input, jokers=False):
    new_order = rank_order(input, jokers)
    total = 0
    i = 1

    for val in new_order:
        bid = int(val[7:])
        total += bid * i
        i += 1

    return total


def test_solve_puzzle(day7_input):

    assert solve_puzzle(example_input) == 6440
    assert solve_puzzle(example_input, jokers=True) == 5905

    assert solve_puzzle(day7_input) == 251806792
    assert solve_puzzle(day7_input, jokers=True) == 252113488


def rank_order(input, jokers=False):
    if jokers:
        mapping_table = str.maketrans(
            {'A': 'E', 'K': 'D', 'Q': 'C', 'J': '1', 'T': 'A'})
    else:
        mapping_table = str.maketrans(
            {'A': 'E', 'K': 'D', 'Q': 'C', 'J': 'B', 'T': 'A'})
    new_order = []

    for val in input.splitlines():
        rank = get_hand(val, jokers)
        new_val = val.translate(mapping_table)
        new_order.append(rank+new_val)

    new_order.sort()
    return new_order


def test_rank_order():

    assert rank_order(example_input)[0] == 'I32A3D 765'
    assert rank_order(example_input)[1] == 'JDABBA 220'
    assert rank_order(example_input)[2] == 'JDD677 28'
    assert rank_order(example_input)[3] == 'KA55B5 684'
    assert rank_order(example_input)[4] == 'KCCCBE 483'

    assert rank_order(example_input, jokers=True)[4] == 'MDA11A 220'


def get_hand(input, jokers=False):
    hand = input[:5]
    if jokers:
        hand = jokerify(hand)

    card_counts = list({card: hand.count(card) for card in hand}.values())

    len_cc = len(card_counts)
    if len_cc == 1:
        # fives
        return 'N'
    elif len_cc == 2:
        if 4 in card_counts:
            # fours
            return 'M'
        else:
            # fullhouse
            return 'L'
    elif len_cc == 3:
        if 3 in card_counts:
            # threes
            return 'K'
        else:
            # two pairs
            return 'J'
    elif len_cc == 4:
        # pair
        return 'I'
    # ace
    return 'H'

def test_get_hand():
    assert get_hand('QTTTT 32') == 'M'
    assert get_hand('2TT2T 9') == 'L'
    assert get_hand('23T2T 4') == 'J'
    assert get_hand('23T22 43') == 'K'
    assert get_hand('73T22 235') == 'I'
    assert get_hand('73TA2 12') == 'H'

def jokerify(hand):
    if not 'J' in hand or hand == 'JJJJJ':
        return hand

    dictified = {card: hand.count(card) for card in hand}

    largest_non_joker = ''
    largest_non_joker_amount = 0
    for key in dictified:
        if key != 'J':
            if dictified[key] > largest_non_joker_amount:
                largest_non_joker_amount = dictified[key]
                largest_non_joker = key

    new_hand = hand.replace('J', largest_non_joker)

    return new_hand


def test_jokerify():
    assert jokerify('TTTTJ') == 'TTTTT'
    assert jokerify('TTTT6') == 'TTTT6'
    assert jokerify('TTKKJ') == 'TTKKT'
    assert jokerify('2345J') == '23452'
    assert jokerify('KTJJT') == 'KTTTT'
    assert jokerify('JJJJJ') == 'JJJJJ'


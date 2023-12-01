import pytest
c_values = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

puzzle_input = """FILTERED"""

textual_numbers = ['notexisting', 'one', 'two', 'three', 'four', 'five',
                   'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def get_first_and_last_digit_in_string(line):
    first_index = 999
    first_value = ''
    last_index = -999
    last_value = ''

    for val in textual_numbers:
        try:
            ind = line.index(val)
            if ind < first_index:
                first_index = ind
                first_value = val
        except:
            continue
        try:
            ind = line.rindex(val)
            if ind > last_index:
                last_index = ind
                last_value = val
        except:
            continue

    return first_value, last_value


def test_get_first_and_last_digit_in_string():
    i, j = get_first_and_last_digit_in_string("two1nine")
    assert i == "two"
    assert j == "nine"

    i, j = get_first_and_last_digit_in_string("seven")
    assert i == "seven"
    assert j == "seven"


def convert_to_num(text):
    try:
        int(text)
        return text
    except:
        for idx, val in enumerate(textual_numbers):
            if val == text:
                return str(idx)


def decode_calibration(line):
    first, last = get_first_and_last_digit_in_string(line)
    return convert_to_num(first) + convert_to_num(last)


def decode_calibration_list(lines):
    sum = 0
    for line in lines.split():
        sum += int(decode_calibration(line))
    return sum

def test_convert_to_num():
    assert convert_to_num("one") == "1"
    assert convert_to_num("7") == "7"


def test_decode_calibration():
    assert decode_calibration("1abc2") == "12"
    assert decode_calibration("nine1abc2four") == "94"
    assert decode_calibration("seven") == "77"


def test_calibration_list():
    assert decode_calibration_list(c_values) == 142
    assert decode_calibration_list(puzzle_input) == 54578

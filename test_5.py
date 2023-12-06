
class Range:

    def __init__(self, text) -> None:
        lst = [int(x) for x in text.split()]
        self.source = lst[1]
        self.destination = lst[0]
        self.range = lst[2]

    def transport(self, item):
        if self.source <= item <= self.source + self.range:
            return self.destination + (item - self.source)
        else:
            return item

def pass_range_list(range_list, item):
    new_val = 0
    for text_range in range_list.splitlines():
        range = Range(text_range)
        new_val = range.transport(item)
        if new_val != item:
            return new_val
        
    return new_val

def solve_puzzle(input, seeds):
    soil = to_soil_map(input)
    fertilizer = to_fertilizer_map(input)
    water = to_water_map(input)
    light = to_light_map(input)
    temperature = to_temperature_map(input)
    humidity = to_humidity_map(input)
    location = to_location_map(input)

    lowest_location = 99999999999

    for seed in seeds:
        new_value = seed

        #go thru soil
        new_value = pass_range_list(soil, new_value)
        new_value = pass_range_list(fertilizer, new_value)
        new_value = pass_range_list(water, new_value)
        new_value = pass_range_list(light, new_value)
        new_value = pass_range_list(temperature, new_value)
        new_value = pass_range_list(humidity, new_value)
        new_value = pass_range_list(location, new_value)

        if new_value < lowest_location:
            lowest_location = new_value
    
    return lowest_location


def test_range():
    range = Range('50 98 2')
    assert range.source == 98
    assert range.destination == 50
    assert range.range == 2

def test_range_transport():
    item1 = 12
    item2 = 99
    range = Range('50 98 2')

    assert range.transport(item1) == 12
    assert range.transport(item2) == 51

seed_to_soil_example = """50 98 2
52 50 48"""
def test_pass_range_list():
    item1 = 4
    item2 = 98
    assert pass_range_list(seed_to_soil_example, item1) == 4
    assert pass_range_list(seed_to_soil_example, item2) == 50

def test_puzzle_1(day5_input):
    seeds = to_seeds(input_example)
    assert solve_puzzle(input_example, seeds) == 35
    seeds = to_seeds(day5_input)
    assert solve_puzzle(day5_input, seeds) == 174137457

def test_puzzle_2(day5_input):
    seeds = to_seeds_long(input_example)
    assert solve_puzzle(input_example, seeds) == 46




input_example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def to_seeds(input):
    return [int(x) for x in input[input.index('seeds:')+7:input.index('seed-to-soil map:')-2].split()]

def to_seeds_long(input):
    seeds = [int(x) for x in to_seeds(input)]
    long_seeds = []
    for i in range(0, len(seeds), 2):
        seed_start = seeds[i]
        seed_count = seeds[i+1]
        breakpoint()
        for i in range(seed_count):
            long_seeds.append(seed_start+i)

    return long_seeds

def to_soil_map(input):
    return input[input.index('seed-to-soil map:')+18:input.index('soil-to-fertilizer map:')-2]

def to_fertilizer_map(input):
    return input[input.index('soil-to-fertilizer map:')+24:input.index('fertilizer-to-water map:')-2]

def to_water_map(input):
    return input[input.index('fertilizer-to-water map:')+25:input.index('water-to-light map:')-2]

def to_light_map(input):
    return input[input.index('water-to-light map:')+20:input.index('light-to-temperature map:')-2]

def to_temperature_map(input):
    return input[input.index('light-to-temperature map:')+26:input.index('temperature-to-humidity map:')-2]

def to_humidity_map(input):
    return input[input.index('temperature-to-humidity map:')+29:input.index('humidity-to-location map:')-2]

def to_location_map(input):
    return input[input.index('humidity-to-location map:')+26:]

def test_input_handling():
    assert to_seeds(input_example) == [79,14,55,13]
    long_seeds = to_seeds_long(input_example)
    assert long_seeds[1] == 80
    assert len(long_seeds) == 27
    assert to_soil_map(input_example) == """50 98 2
52 50 48"""

    assert to_soil_map(input_example) == """50 98 2
52 50 48"""

    assert to_fertilizer_map(input_example) == """0 15 37
37 52 2
39 0 15"""

    assert to_water_map(input_example) == """49 53 8
0 11 42
42 0 7
57 7 4"""

    assert to_light_map(input_example) == """88 18 7
18 25 70"""

    assert to_temperature_map(input_example) == """45 77 23
81 45 19
68 64 13"""

    assert to_humidity_map(input_example) == """0 69 1
1 0 69"""

    assert to_location_map(input_example) == """60 56 37
56 93 4"""

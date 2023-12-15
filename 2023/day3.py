# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water
# source, but this is as far as he can bring you. You go inside.
#
# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.
#
# "Aah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting
# anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.
#
# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one.
# If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.
#
# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of
# numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally,
# is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
#
# Here is an example engine schematic:
#
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#
# In
# this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58
# (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine
# schematic?
import itertools

from utils import read_file_to_array
from itertools import product
from collections import defaultdict


def calc(schematic: list):
    symbols = {'%', '#', '=', '$', '&', '*', '-', '+', '@', '/'}
    numbers = []
    coordinates = []
    gears = defaultdict(list)
    total = 0
    total_hard = 0

    for i in range(len(schematic)):
        j = 0
        while j < len(schematic[i]):
            number, coords = [], []

            while j < len(schematic[i]) and schematic[i][j].isnumeric():
                number.append(schematic[i][j])
                coords.append((i, j))
                j += 1

            if number:
                numbers.append(''.join(number))
                coordinates.append(coords)

            j += 1

    for i in range(len(numbers)):
        for c in list(product(range(-1, 2), repeat=2)):
            li, lj = tuple(sum(coord) for coord in zip(coordinates[i][0], c))
            ri, rj = tuple(sum(coord) for coord in zip(coordinates[i][-1], c))
            if li < len(schematic) and lj < len(schematic[0]) and schematic[li][lj] in symbols\
                    or ri < len(schematic) and rj < len(schematic[0]) and schematic[ri][rj] in symbols:
                total += int(numbers[i])

                if schematic[li][lj] == '*':
                    gears[(li, lj)].append(numbers[i])

                elif schematic[ri][rj] == '*':
                    gears[(ri, rj)].append(numbers[i])

                break

    asdf = {}
    for key, val in gears.items():
        asdf[key] = val
        if len(val) == 2:
            total_hard += (int(val[0]) * int(val[1]))

    print(asdf)
    return total, total_hard


if __name__ == '__main__':
    engine_schematic = read_file_to_array('inputs/day3.txt')
    easy, hard = calc(engine_schematic)
    print(f'Easy: {easy}')
    print(f'Hard: {hard}')




from utils import read_file_to_array
from itertools import combinations

def find_empty(galaxies: list):
    empty_rows = set([i for i, row in enumerate(galaxies) if all(char == '.' for char in row)])
    empty_cols = set([j for j, col in enumerate(zip(*galaxies)) if all(char == '.' for char in col)])

    return empty_rows, empty_cols


def find_poi_list(galaxies: list) -> list :
    poi = []
    for i, row in enumerate(galaxies):
        for j, char in enumerate(row):
            if char == '#':
                poi.append((i, j))

    return list(combinations(poi, r=2))


def calc_total_min_distance(galaxies: list, part2=False):
    empty_rows, empty_cols = find_empty(galaxies=galaxies)
    poi_list = find_poi_list(galaxies)
    total = 0

    for p1, p2 in poi_list:
        p1i, p1j = p1
        p2i, p2j = p2
        # check i
        for i in range(min(p1i, p2i), max(p1i, p2i)):
            if i in empty_rows and part2:
                total += 999999
            elif i in empty_rows:
                total += 1
            total += 1
        # check j
        for j in range(min(p1j, p2j), max(p1j, p2j)):
            if j in empty_cols and part2:
                total += 999999
            elif j in empty_cols:
                total += 1
            total += 1

    return total


if __name__ == '__main__':
    galaxies = read_file_to_array('inputs/day11.txt')

    print(f'Easy: {calc_total_min_distance(galaxies=galaxies)}')
    print(f'Hard: {calc_total_min_distance(galaxies=galaxies, part2=True)}')

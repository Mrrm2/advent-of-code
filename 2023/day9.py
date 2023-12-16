import copy

from utils import read_file_to_array


def build_right(pyramid: list[list]) -> tuple:
    curr_right, curr_left = 0, 0
    for i in range(len(pyramid) - 2, -1, -1):
        curr_right += pyramid[i][-1]
        curr_left = pyramid[i][0] - curr_left

    return curr_right, curr_left


def calc(file: list):
    right, left = 0, 0
    pyramids = []
    for row in file:
        pyramid = [row]
        while True:
            next_row = []
            for i, val in enumerate(pyramid[-1][:-1]):
                next_row.append(pyramid[-1][i + 1] - val)
            pyramid.append(next_row)
            if all(value == 0 for value in next_row):
                break

        pyramids.append(pyramid)

    for pyramid in pyramids:
        r, l = build_right(pyramid)
        right += r
        left += l

    return right, left


if __name__ == '__main__':
    file = read_file_to_array('inputs/day9.txt')
    file = [[int(val) for val in line.split()] for line in file]
    print(f'easy, hard: {calc(file)}')


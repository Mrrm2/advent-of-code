import math
import itertools

from utils import read_file_to_array


def easy(path: str, curr: str, mapping: dict) -> int:
    res = 0
    path = itertools.cycle(path)
    while curr != 'ZZZ':
        curr = mapping.get(curr)[0] if next(path) == 'L' else mapping.get(curr)[1]
        res += 1
    return res


def hard(path: str, mapping: dict) -> int:
    starts, ends = {}, set()
    for k in mapping.keys():
        if k.endswith('A'):
            starts[k] = 0
        elif k.endswith('Z'):
            ends.add(k)

    cycles = []
    for start in starts:
        instruction = itertools.cycle(path)
        curr_cycle = []
        steps = 0
        first_z = None
        curr_location = start
        while True:
            curr_location = mapping.get(curr_location)[0] if next(instruction) == 'L' else mapping.get(curr_location)[1]
            steps += 1
            if curr_location in ends:
                curr_cycle.append(steps)
                steps = 0
                if not first_z:
                    first_z = curr_location
                elif first_z == curr_location:
                    break

        cycles.append(curr_cycle)

    nums = [cycle[0] for cycle in cycles]
    return math.lcm(*nums)


if __name__ == '__main__':
    path, *maps = read_file_to_array('inputs/day8.txt')
    mapping = {k: v.strip('()').split(', ') for line in maps[1:] for k, v in [line.split(' = ')]}
    start = 'AAA'

    print(f'Easy: {easy(path, start, mapping)}')
    print(f'Hard: {hard(path, mapping)}')

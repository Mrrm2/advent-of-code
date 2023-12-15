import json
from functools import reduce


def easy(seed: int, mappings: dict) -> int:
    for mapping in mappings.splitlines()[1:]:
        destination, source, step = map(int, mapping.split())
        if seed in range(source, source + step + 1):
            diff = seed - source
            return destination + diff
    return seed


def hard(seeds: list, mappings: list):
    hard_seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    for mapping in mappings:
        ranges = []
        for line in mapping.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        new = []
        while hard_seeds:
            start, end = hard_seeds.pop()
            for dest, src, r in ranges:
                o_start = max(start, src)
                o_end = min(end, src + r)
                if o_start < o_end:
                    new.append((o_start - src + dest, o_end - src + dest))
                    if o_start > start:
                        hard_seeds.append((start, o_start))
                    if end > o_end:
                        hard_seeds.append((o_end, end))
                    break
            else:
                new.append((start, end))
        hard_seeds = new

    return min(hard_seeds)[0]


if __name__ == '__main__':
    with open('inputs/day5.txt') as f:
        seed_dict, *mappings = f.read().split('\n\n')

    seed_dict = seed_dict.split(':')[1].split()
    seeds = list(map(int, seed_dict))

    print(f'Easy: {min(reduce(easy, mappings, seed) for seed in seeds)}')
    print(f'Hard: {hard(seeds, mappings)}')

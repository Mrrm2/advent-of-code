from functools import reduce
from operator import mul
from utils import read_file_to_array


def easy(times: list, records: list):
    res = 1
    for time, record in zip(times, records):
        wins = 0
        for t in range(time):
            remaining = time - t
            if remaining * t > record:
                wins += 1
        res *= wins

    return res


def hard(time, record):
    wins = 0
    for t in range(time):
        remaining = time - t
        if remaining * t > record:
            wins += 1

    return wins


if __name__ == '__main__':
    file = read_file_to_array('inputs/day6.txt')

    times = list(map(int, (file[0].split(':')[1].split())))
    records = list(map(int, (file[1].split(':')[1].split())))

    print(f'Easy: {easy(times, records)}')
    print(f'Hard: {hard(int(''.join(file[0].split(':')[1].split())), 
                        int(''.join(file[1].split(':')[1].split())))}')

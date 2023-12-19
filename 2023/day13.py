from utils import read_file_to_array
path = 'inputs/day13.txt'


def find_one_off(block):
    for i in range(1, len(block)):
        top = block[:i][::-1]
        bottom = block[i:]

        top = top[:len(bottom)]
        bottom = bottom[:len(top)]

        total = 0
        for t, b in zip(top, bottom):
            for x, y in zip(t, b):
                total += x != y
        if total == 1:
            return i
    return 0


def find_reflection(block):
    for i in range(1, len(block)):
        top = block[:i][::-1]
        bottom = block[i:]

        top = top[:len(bottom)]
        bottom = bottom[:len(top)]

        if top == bottom:
            return i
    return 0


def run(data: list, p1=True):
    total = 0
    for block in data:
        block = block.splitlines()
        if p1:
            horizontal = find_reflection(block)
            total += 100 * horizontal

            vertical = find_reflection(list(zip(*block)))
            total += vertical
        else:
            horizontal = find_one_off(block)
            total += 100 * horizontal

            vertical = find_one_off(list(zip(*block)))
            total += vertical

    return total


if __name__ == '__main__':
    with open(path) as f:
        file = f.read().split('\n\n')

    print(f'Easy: {run(file, p1=True)}')
    print(f'Hard: {run(file, p1=False)}')

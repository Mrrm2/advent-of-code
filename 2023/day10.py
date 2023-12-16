from collections import deque
from timeit import timeit


def easy_pathing(maze: list[str], start: tuple) -> tuple:
    seen = {start}
    q = deque([start])
    s_possible = {'|', '-', 'J', 'L', '7', 'F'}

    while q:
        i, j = q.popleft()
        char = maze[i][j]

        # check up
        if i > 0 and (i - 1, j) not in seen and char in 'S|JL' and maze[i - 1][j] in 'F|7':
            coords = (i - 1, j)
            q.append(coords)
            seen.add(coords)
            if char == 'S':
                s_possible &= {'|', 'J', 'L'}
        # check down
        if i < len(maze) - 1 and (i + 1, j) not in seen and char in 'S|F7' and maze[i + 1][j] in '|JL':
            coords = (i + 1, j)
            q.append(coords)
            seen.add(coords)
            if char == 'S':
                s_possible &= {'|', 'F', '7'}
        # check left
        if j > 0 and (i, j - 1) not in seen and char in 'S-7J' and maze[i][j - 1] in 'LF-':
            coords = (i, j - 1)
            q.append(coords)
            seen.add(coords)
            if char == 'S':
                s_possible &= {'-', '7', 'J'}
        # check right
        if j < len(maze[0]) - 1 and (i, j + 1) not in seen and char in 'S-LF' and maze[i][j + 1] in '7J-':
            coords = (i, j + 1)
            q.append(coords)
            seen.add(coords)
            if char == 'S':
                s_possible &= {'-', 'L', 'F'}

    (s_val, ) = s_possible
    maze = _remove_outside_loop(maze, seen, s_val)

    return len(seen) // 2, maze, seen


def easy_linear(maze: list[str], start: tuple) -> int:
    seen = {start}
    curr = start
    while True:
        i, j = curr
        char = maze[i][j]
        # check up
        if i > 0 and (i - 1, j) not in seen and char in 'S|JL' and maze[i - 1][j] in 'F|7':
            coords = (i - 1, j)
            seen.add(coords)
            curr = coords

        # check down
        elif i < len(maze) - 1 and (i + 1, j) not in seen and char in 'S|F7' and maze[i + 1][j] in '|JL':
            coords = (i + 1, j)
            seen.add(coords)
            curr = coords

        # check left
        elif j > 0 and (i, j - 1) not in seen and char in 'S-7J' and maze[i][j - 1] in 'LF-':
            coords = (i, j - 1)
            seen.add(coords)
            curr = coords

        # check right
        elif j < len(maze[0]) - 1 and (i, j + 1) not in seen and char in 'S-LF' and maze[i][j + 1] in '7J-':
            coords = (i, j + 1)
            seen.add(coords)
            curr = coords

        else:
            break

    return len(seen) // 2


def _remove_outside_loop(maze: list, loop: set, s_val: str) -> list:
    updated_maze = []
    for i, row in enumerate(maze):
        updated_row = ""
        for j, char in enumerate(row):
            if char == 'S':
                updated_row += s_val
                continue
            if (i, j) in loop:
                updated_row += char
            else:
                updated_row += "."
        updated_maze.append(updated_row)
    return updated_maze


def hard(maze, loop):
    in_set = set()
    for i, row in enumerate(maze):
        inside = False
        up = None
        for j, char in enumerate(row):
            if char == '|':
                inside = not inside
            elif char in '-':
                assert up is not None
            elif char in 'FL':
                up = char == 'L'
            elif char in 'J7':
                if char == ('7' if up else 'J'):
                    inside = not inside
                up = None
            elif char == '.':
                pass
            if inside:
                in_set.add((i, j))

    # for i, row in enumerate(maze):
    #     for j, char in enumerate(row):
    #         print('.' if (i,j) in (in_set - loop) else '#', end='')
    #     print()

    return len(in_set - loop)


if __name__ == '__main__':
    with open('inputs/day10.txt') as f:
        maze = f.read().strip().splitlines()

    start = next((i, j) for i, row in enumerate(maze) for j, char in enumerate(row) if char == 'S')

    time, maze, loop = easy_pathing(maze=maze, start=start)
    # print('\n'.join(maze))
    print(f'Easy: {time}')
    # print(f'Easy: {easy_linear(maze=maze, start=start)}')
    print(f'Hard: {hard(maze, loop)}')

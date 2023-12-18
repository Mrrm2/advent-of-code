from utils import read_file_to_array
from functools import cache


@cache
def count_location(nums: tuple, spring_group: list, res=0) -> int:
    if not nums:
        return '#' not in spring_group

    curr, nums = nums[0], nums[1:]

    for i in range(len(spring_group) - sum(nums) - len(nums) - curr + 1):
        if "#" in spring_group[:i]:
            break
        # valid spot if length spring_group[x:] >= number and all(spot in '$?' for spot spring_group)
        next = i + curr
        if next <= len(spring_group) and '.' not in spring_group[i: next] and spring_group[next: next + 1] != "#":
            res += count_location(nums, spring_group[next + 1:])
    return res


if __name__ == '__main__':
    f = read_file_to_array('inputs/day12.txt')

    easy, hard = 0, 0
    for line in f:
        spring_group, nums = line.split()
        nums = tuple(map(int, nums.split(',')))
        easy += count_location(nums, spring_group)

        # hard
        spring_group = '?'.join([spring_group] * 5)
        nums *= 5
        hard += count_location(nums, spring_group)

    print(f'Easy: {easy}')
    print(f'Hard: {hard}')

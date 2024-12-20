#!/usr/bin/env python3

from itertools import pairwise


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    input = []
    for line in lines:
        nums = [int(n) for n in line.split(" ")]
        input.append(nums)

    return input


def test_parse_input():
    test_lines = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
    assert parse_input(test_lines.strip().split("\n")) == [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]


def test_is_level_safe():
    assert is_level_safe([7, 6, 4, 2, 1]) is True
    assert is_level_safe([1, 2, 7, 8, 9]) is False
    assert is_level_safe([9, 7, 6, 2, 1]) is False
    assert is_level_safe([1, 3, 2, 4, 5]) is False
    assert is_level_safe([8, 6, 4, 4, 1]) is False
    assert is_level_safe([1, 3, 6, 7, 9]) is True


def is_level_safe(level):
    increments = 0
    decrements = 0

    for a, b in pairwise(level):
        if abs(a - b) < 1 or abs(a - b) > 3:
            return False

        if a < b:
            increments += 1
        elif a > b:
            decrements += 1

    if increments > 0 and decrements > 0:
        return False

    return True


def solve_part_1(input):

    safe = 0

    for level in input:
        if is_level_safe(level):
            safe += 1

    return safe


def test_solve_part_1():
    test_input = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert solve_part_1(test_input) == 2


def solve_part_2(input):
    safe = 0

    for level in input:
        if is_level_safe(level):
            safe += 1
            continue

        for i in range(len(level)):
            level_copy = level.copy()
            level_copy.pop(i)

            if is_level_safe(level_copy):
                safe += 1
                break

    return safe


def test_solve_part_2():
    test_input = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9],
    ]
    assert solve_part_2(test_input) == 4


if __name__ == "__main__":
    sample = parse_input(read_input("02/sample.txt"))
    input = parse_input(read_input("02/input.txt"))
    print(f"part 1 sample {solve_part_1(sample)}")
    print(f"part 1 solution {solve_part_1(input)}")

    print(f"part 2 sample {solve_part_2(sample)}")
    print(f"part 2 solution {solve_part_2(input)}")

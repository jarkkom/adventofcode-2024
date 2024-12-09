#!/usr/bin/env python3

from pprint import pprint
from itertools import pairwise


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    input = []
    for l in lines:
        nums = [int(n) for n in l.split(" ")]
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
    is_level_safe([7, 6, 4, 2, 1]) == True
    is_level_safe([1, 2, 7, 8, 9]) == False
    is_level_safe([9, 7, 6, 2, 1]) == False
    is_level_safe([1, 3, 2, 4, 5]) == False
    is_level_safe([8, 6, 4, 4, 1]) == False
    is_level_safe([1, 3, 6, 7, 9]) == True


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
    print(solve_part_1(parse_input(read_input("02/sample.txt"))))
    print(solve_part_1(parse_input(read_input("02/input.txt"))))

    print(solve_part_2(parse_input(read_input("02/sample.txt"))))
    print(solve_part_2(parse_input(read_input("02/input.txt"))))

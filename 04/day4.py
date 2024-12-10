#!/usr/bin/env python3

# from pprint import pprint


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    input = []
    for line in lines:
        row = []
        for c in line:
            row.append(c)
        input.append(row)

    return input


def test_parse_input():
    test_lines = """
..X...
.SAMX.
.A..A.
XMAS.S
.X...."""
    assert parse_input(test_lines.strip().split("\n")) == [
        [".", ".", "X", ".", ".", "."],
        [".", "S", "A", "M", "X", "."],
        [".", "A", ".", ".", "A", "."],
        ["X", "M", "A", "S", ".", "S"],
        [".", "X", ".", ".", ".", "."],
    ]


def check_x(input, x, y, dx, dy):
    y_max = len(input)
    x_max = len(input[0])

    letters = ["X", "M", "A", "S"]

    while True:
        letter = letters.pop(0)
        if input[y][x] != letter:
            return False

        if len(letters) == 0:
            return True

        x += dx
        y += dy
        if x < 0 or x >= x_max or y < 0 or y >= y_max:
            return False


def solve_part_1(input):
    found = 0
    for y, row in enumerate(input):
        for x, c in enumerate(row):
            if c == "X":
                if check_x(input, x, y, -1, -1):
                    found += 1
                if check_x(input, x, y, 0, -1):
                    found += 1
                if check_x(input, x, y, 1, -1):
                    found += 1
                if check_x(input, x, y, -1, 0):
                    found += 1
                if check_x(input, x, y, 1, 0):
                    found += 1
                if check_x(input, x, y, -1, 1):
                    found += 1
                if check_x(input, x, y, 0, 1):
                    found += 1
                if check_x(input, x, y, 1, 1):
                    found += 1

    return found


def test_solve_part_1():
    test_input = [
        [".", ".", "X", ".", ".", "."],
        [".", "S", "A", "M", "X", "."],
        [".", "A", ".", ".", "A", "."],
        ["X", "M", "A", "S", ".", "S"],
        [".", "X", ".", ".", ".", "."],
    ]
    assert solve_part_1(test_input) == 4


def check_xmas(input, x, y):
    count_m = 0
    count_s = 0

    for dx, dy in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
        if input[y + dy][x + dx] == "M" and input[y - dy][x - dx] == "S":
            count_m += 1

        if input[y + dy][x + dx] == "S" and input[y - dy][x - dx] == "M":
            count_s += 1

    if count_m == 2 and count_s == 2:
        return True


def solve_part_2(input):
    found = 0

    y_max = len(input)
    x_max = len(input[0])

    for y, row in enumerate(input):
        for x, c in enumerate(row):
            if x < 1 or y < 1 or x >= x_max - 1 or y >= y_max - 1:
                continue

            if c == "A":
                if check_xmas(input, x, y):
                    found += 1

    return found


def test_solve_part_2():
    test_input = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""
    parsed_input = parse_input(test_input.strip().split("\n"))
    assert solve_part_2(parsed_input) == 9


if __name__ == "__main__":
    sample = parse_input(read_input("04/sample.txt"))
    input = parse_input(read_input("04/input.txt"))
    print(f"part 1 sample {solve_part_1(sample)}")
    print(f"part 1 {solve_part_1(input)}")

    print(f"part 2 sample {solve_part_2(sample)}")
    print(f"part 2 {solve_part_2(input)}")

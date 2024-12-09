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


if __name__ == "__main__":
    sample = parse_input(read_input("04/sample.txt"))
    input = parse_input(read_input("04/input.txt"))
    print(f"part 1 sample {solve_part_1(sample)}")
    print(f"part 1 {solve_part_1(input)}")

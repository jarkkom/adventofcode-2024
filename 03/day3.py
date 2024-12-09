#!/usr/bin/env python3

# from pprint import pprint
import re


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    input = []
    for line in lines:
        muls = re.findall(r"mul\((\d+),(\d+)\)", line)
        input.append(muls)

    return input


def test_parse_input():
    test_lines = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    assert parse_input(test_lines.strip().split("\n")) == [
        [("2", "4"), ("5", "5"), ("11", "8"), ("8", "5")]
    ]


def solve_part_1(input):
    total = 0
    for line in input:
        for mul in line:
            (a, b) = mul
            total += int(a) * int(b)
    return total


def test_solve_part_1():
    test_input = [[("2", "4"), ("5", "5"), ("11", "8"), ("8", "5")]]
    assert solve_part_1(test_input) == 161


def solve_part_2(input):
    pass


def test_solve_part_2():
    pass


if __name__ == "__main__":
    sample = parse_input(read_input("03/sample.txt"))
    input = parse_input(read_input("03/input.txt"))
    print(f"part 1 sample {solve_part_1(sample)}")
    print(f"part 1 solution {solve_part_1(input)}")

    print(f"part 2 sample {solve_part_2(sample)}")
    print(f"part 2 solution {solve_part_2(input)}")

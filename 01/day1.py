#!/usr/bin/env python3


from pprint import pprint


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    input = []

    for l in lines:
        nums = [int(n) for n in l.split("   ")]
        input.append(nums)

    return input


def test_parse_input():
    test_lines = """
3   4
4   3
2   5
1   3
3   9
3   3"""
    assert parse_input(test_lines.strip().split("\n")) == [
        [3, 4],
        [4, 3],
        [2, 5],
        [1, 3],
        [3, 9],
        [3, 3],
    ]


def solve_part_1(input):

    a = []
    b = []

    for i in input:
        (aa, bb) = i

        a.append(aa)
        b.append(bb)

    a.sort()
    b.sort()

    distance_sum = 0
    for left, right in zip(a, b):
        distance_sum += abs(int(left) - int(right))

    return distance_sum


def test_solve_part_1():
    test_input = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
    assert solve_part_1(test_input) == 11


def solve_part_2(input):
    a = []
    b = []

    for i in input:
        (aa, bb) = i

        a.append(aa)
        b.append(bb)

    similarity_score = 0
    for aa in a:
        similarity_score += int(aa) * b.count(aa)

    return similarity_score


def test_solve_part_2():
    test_input = [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 3]]
    assert solve_part_2(test_input) == 31


if __name__ == "__main__":
    sample = parse_input(read_input("01/sample.txt"))
    input = parse_input(read_input("01/input.txt"))
    print(f"part 1 sample {solve_part_1(sample)}")
    print(f"part 1 solution {solve_part_1(input)}")

    print(f"part 2 sample {solve_part_2(sample)}")
    print(f"part 2 solution {solve_part_2(input)}")

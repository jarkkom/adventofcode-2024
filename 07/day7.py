#!/usr/bin/env python3

import itertools


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    inputs = []

    for line in lines:
        if line == "":
            continue

        (result, operands) = line.split(": ", 2)

        inputs.append((result, operands.split(" ")))

    return inputs


def test_parse_input():
    test_lines = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip().split(
        "\n"
    )
    assert parse_input(test_lines) == [
        ("190", ["10", "19"]),
        ("3267", ["81", "40", "27"]),
        ("83", ["17", "5"]),
        ("156", ["15", "6"]),
        ("7290", ["6", "8", "6", "15"]),
        ("161011", ["16", "10", "13"]),
        ("192", ["17", "8", "14"]),
        ("21037", ["9", "7", "18", "13"]),
        ("292", ["11", "6", "16", "20"]),
    ]


def solve_part_1(inputs):
    total = 0

    for result, operand_list in inputs:
        operations_tuples = list(
            itertools.product(["+", "*"], repeat=len(operand_list) - 1)
        )
        operations = [list(perm) for perm in operations_tuples]

        for operation in operations:
            ix = 1
            acc = int(operand_list[0])

            while ix < len(operand_list):
                if operation[ix - 1] == "+":
                    acc += int(operand_list[ix])
                else:
                    acc *= int(operand_list[ix])

                ix += 1

            if acc == int(result):
                total += acc
                break

            # print(f"{operand_list} {operation} = {acc}")

    return total


def test_solve_part_1():
    test_input = parse_input(
        """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
            "\n"
        )
    )
    assert solve_part_1(test_input) == 3749


def solve_part_2(inputs):
    total = 0

    for result, operand_list in inputs:
        operations_tuples = list(
            itertools.product(["+", "*", "|"], repeat=len(operand_list) - 1)
        )
        operations = [list(perm) for perm in operations_tuples]

        for operation in operations:
            ix = 1
            acc = int(operand_list[0])

            while ix < len(operand_list):
                if operation[ix - 1] == "+":
                    acc += int(operand_list[ix])
                elif operation[ix - 1] == "*":
                    acc *= int(operand_list[ix])
                else:
                    acc = int(f"{acc}{operand_list[ix]}")

                ix += 1

            if acc == int(result):
                total += acc
                break

    return total


def test_solve_part_2():
    test_input = parse_input(
        """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
            "\n"
        )
    )
    assert solve_part_2(test_input) == 11387


if __name__ == "__main__":
    sample = parse_input(read_input("07/sample.txt"))
    input = parse_input(read_input("07/input.txt"))

    print(f"part 1 sample = {solve_part_1(sample)}")
    print(f"part 1 input = {solve_part_1(input)}")

    print(f"part 2 sample = {solve_part_2(sample)}")
    print(f"part 2 input = {solve_part_2(input)}")

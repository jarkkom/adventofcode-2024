#!/usr/bin/env python3


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()


def parse_input(input):
    blocks = []

    file_id = 0
    free = False
    for count in input:
        if not free:
            for _ in range(int(count)):
                blocks.append(file_id)
            file_id += 1
            free = True
        else:
            for _ in range(int(count)):
                blocks.append(-1)
            free = False

    return blocks


def test_parse_input():
    test_1 = parse_input("12345")
    assert test_1 == [0, -1, -1, 1, 1, 1, -1, -1, -1, -1, 2, 2, 2, 2, 2]

    test_2 = parse_input("2333133121414131402")
    assert test_2 == [
        0,
        0,
        -1,
        -1,
        -1,
        1,
        1,
        1,
        -1,
        -1,
        -1,
        2,
        -1,
        -1,
        -1,
        3,
        3,
        3,
        -1,
        4,
        4,
        -1,
        5,
        5,
        5,
        5,
        -1,
        6,
        6,
        6,
        6,
        -1,
        7,
        7,
        7,
        -1,
        8,
        8,
        8,
        8,
        9,
        9,
    ]


def solve_part_1(blocks):
    head = 0

    tail = len(blocks) - 1

    while head < tail:
        # find first free block
        while blocks[head] != -1:
            head += 1

        # find last used block
        while blocks[tail] == -1:
            tail -= 1

        if head >= tail:
            break

        blocks[head] = blocks[tail]
        blocks[tail] = -1

    checksum = 0
    for block, file in enumerate(blocks):
        if file == -1:
            continue
        checksum += block * file

    return checksum


if __name__ == "__main__":
    sample = read_input("09/sample.txt")
    input = read_input("09/input.txt")

    print(f"part 1 sample = {solve_part_1(parse_input(sample))}")
    print(f"part 1 sample = {solve_part_1(parse_input(input))}")

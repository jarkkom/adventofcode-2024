#!/usr/bin/env python3


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    map = []
    sx = None
    sy = None

    for y, line in enumerate(lines):
        row = []
        if line == "":
            continue

        for x, c in enumerate(line):
            if c == "^":
                row.append(".")
                sx = x
                sy = y
            else:
                row.append(c)

        map.append(row)

    return map, sx, sy


def test_parse_input():
    input = """....#.....
.........#
.#..^.....
"""
    assert parse_input(input.strip().split("\n")) == (
        [
            [".", ".", ".", ".", "#", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
            [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
        ],
        4,
        2,
    )


def solve_part_1(map, sx, sy):
    y_max = len(map)
    x_max = len(map[0])

    x = sx
    y = sy

    dx = 0
    dy = -1

    visited = {}

    while True:
        visited[(x, y)] = True

        if x + dx < 0 or x + dx >= x_max or y + dy < 0 or y + dy >= y_max:
            break

        c = map[y + dy][x + dx]

        if c == "#":
            # turn 90 degrees right
            tmp_dx = dx
            dx = -dy
            dy = tmp_dx

        x += dx
        y += dy

    return len(visited)


def test_solve_part_1():
    test_map, test_sx, test_sy = parse_input(
        """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip().split(
            "\n"
        )
    )
    assert solve_part_1(test_map, test_sx, test_sy) == 41


if __name__ == "__main__":
    sample_map, sample_sx, sample_sy = parse_input(read_input("06/sample.txt"))
    input_map, input_sx, input_sy = parse_input(read_input("06/input.txt"))

    print(f"part 1 sample {solve_part_1(sample_map, sample_sx, sample_sy)}")
    print(f"part 1 input {solve_part_1(input_map, input_sx, input_sy)}")

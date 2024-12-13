#!/usr/bin/env python3


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    map = []
    antennas = {}

    for y, line in enumerate(lines):
        row = []
        if line == "":
            continue

        for x, c in enumerate(line):
            if c != ".":
                if c not in antennas:
                    antennas[c] = [(x, y)]
                else:
                    antennas[c].append((x, y))

            row.append(c)

        map.append(row)

    return map, antennas


def test_parse_input():
    input = """.a.
0.A
.Aa
"""
    test_map, test_antennas = parse_input(input.strip().split("\n"))
    assert test_map == [
        [".", "a", "."],
        ["0", ".", "A"],
        [".", "A", "a"],
    ]
    assert test_antennas == {
        "a": [(1, 0), (2, 2)],
        "0": [(0, 1)],
        "A": [(2, 1), (1, 2)],
    }


def check_antipode(map, x, y, frequency, x_max, y_max):
    return (
        y >= 0
        and y < y_max
        and x >= 0
        and x < x_max
        and map[y][x] != frequency
    )


def solve_part_1(map, antennas):
    y_max = len(map)
    x_max = len(map[0])

    antipodes = []
    for antenna in antennas:
        for coords in antennas[antenna]:
            x, y = coords

            if len(antennas[antenna]) == 1:
                continue

            for compare_ix in range(len(antennas[antenna])):
                x2, y2 = antennas[antenna][compare_ix]

                if x == x2 and y == y2:
                    continue

                dx = x2 - x
                dy = y2 - y

                if check_antipode(map, x + dx, y + dy, antenna, x_max, y_max):
                    antipodes.append((x + dx, y + dy))

                if check_antipode(map, x - dx, y - dy, antenna, x_max, y_max):
                    antipodes.append((x - dx, y - dy))

    # for y in range(y_max):
    #     for x in range(x_max):
    #         if (x, y) in antipodes:
    #             print("#", end="")
    #         else:
    #             print(map[y][x], end="")

    #     print()

    return len(set(antipodes))


def test_solve_part_1():
    test_input__3 = """..........
..........
..........
....a.....
........a.
.....a....
..........
......A...
..........
.........."""
    test_map_3, test_antennas_3 = parse_input(
        test_input__3.strip().split("\n")
    )
    assert solve_part_1(test_map_3, test_antennas_3) == 4

    test_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
    test_map, test_antennas = parse_input(test_input.strip().split("\n"))
    assert solve_part_1(test_map, test_antennas) == 14


def solve_part_2(map, antennas):
    y_max = len(map)
    x_max = len(map[0])

    antipodes = []
    for antenna in antennas:
        for coords in antennas[antenna]:
            x, y = coords

            if len(antennas[antenna]) == 1:
                continue

            for compare_ix in range(len(antennas[antenna])):
                x2, y2 = antennas[antenna][compare_ix]

                if x == x2 and y == y2:
                    continue

                dx = x2 - x
                dy = y2 - y

                ax = x
                ay = y
                while ax >= 0 and ax < x_max and ay >= 0 and ay < y_max:
                    antipodes.append((ax, ay))
                    ax += dx
                    ay += dy

                ax = x
                ay = y
                while ax >= 0 and ax < x_max and ay >= 0 and ay < y_max:
                    antipodes.append((ax, ay))
                    ax -= dx
                    ay -= dy

    # for y in range(y_max):
    #     for x in range(x_max):
    #         if (x, y) in antipodes:
    #             print("#", end="")
    #         else:
    #             print(map[y][x], end="")

    #     print()

    return len(set(antipodes))


def test_solve_part_2():
    test_input__3 = """T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
.........."""
    test_map_3, test_antennas_3 = parse_input(
        test_input__3.strip().split("\n")
    )
    assert solve_part_2(test_map_3, test_antennas_3) == 9


if __name__ == "__main__":
    sample_map, sample_antennas = parse_input(read_input("08/sample.txt"))
    input_map, input_antennas = parse_input(read_input("08/input.txt"))

    print(f"part 1 sample = {solve_part_1(sample_map, sample_antennas)}")
    print(f"part 1 input = {solve_part_1(input_map, input_antennas)}")

    print(f"part 2 sample = {solve_part_2(sample_map, sample_antennas)}")
    print(f"part 2 input = {solve_part_2(input_map, input_antennas)}")

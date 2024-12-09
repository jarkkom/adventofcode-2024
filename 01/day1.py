#!/usr/bin/env python3


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")
    

def solve_part_1(input):

    a = []
    b = []

    for i in input:
        (aa, bb) = i.split("   ", 2)

        a.append(aa)
        b.append(bb)

    a.sort()
    b.sort()

    distance_sum = 0
    for (left, right) in zip(a, b):
        distance_sum += abs(int(left) - int(right))

    return distance_sum


def solve_part_2(input):

    a = []
    b = []

    for i in input:
        (aa, bb) = i.split("   ", 2)

        a.append(aa)
        b.append(bb)


    similarity_score = 0
    for aa in a:
        similarity_score += int(aa) * b.count(aa)

    return similarity_score


if __name__ == "__main__":
    print(solve_part_1(read_input("01/sample.txt")))
    print(solve_part_1(read_input("01/input.txt")))

    print(solve_part_2(read_input("01/sample.txt")))
    print(solve_part_2(read_input("01/input.txt")))

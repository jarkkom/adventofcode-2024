#!/usr/bin/env python3


def read_input(file_path):
    with open(file_path, "r") as file:
        return file.read().strip().split("\n")


def parse_input(lines):
    rules = []
    pages_list = []

    for line in lines:

        if line == "":
            continue

        rule = line.split("|")
        if len(rule) > 1:
            rules.append(rule)

        page_list = line.split(",")
        if len(page_list) > 1:
            pages_list.append(page_list)

    return (rules, pages_list)


def test_parse_input():
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
    assert parse_input(input.strip().split("\n")) == (
        [
            ["47", "53"],
            ["97", "13"],
            ["97", "61"],
            ["97", "47"],
            ["75", "29"],
            ["61", "13"],
            ["75", "53"],
            ["29", "13"],
            ["97", "29"],
            ["53", "29"],
            ["61", "53"],
            ["97", "53"],
            ["61", "29"],
            ["47", "13"],
            ["75", "47"],
            ["97", "75"],
            ["47", "61"],
            ["75", "61"],
            ["47", "29"],
            ["75", "13"],
            ["53", "13"],
        ],
        [
            ["75", "47", "61", "53", "29"],
            ["97", "61", "53", "29", "13"],
            ["75", "29", "13"],
            ["75", "97", "47", "61", "53"],
            ["61", "13", "29"],
            ["97", "13", "75", "29", "47"],
        ],
    )


def solve_part_1(rules, pages_list):

    sum = 0

    for pages in pages_list:

        eligible_rules = []
        for rule in rules:
            before, after = rule
            if before in pages and after in pages:
                eligible_rules.append(rule)

        valid = True
        for ix, page in enumerate(pages):
            for before, after in eligible_rules:
                if page == before and after in pages[:ix]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            middle = pages[len(pages) // 2]
            sum += int(middle)

    return sum


def test_solve_part_1():
    rules = [
        ["47", "53"],
        ["97", "13"],
        ["97", "61"],
        ["97", "47"],
        ["75", "29"],
        ["61", "13"],
        ["75", "53"],
        ["29", "13"],
        ["97", "29"],
        ["53", "29"],
        ["61", "53"],
        ["97", "53"],
        ["61", "29"],
        ["47", "13"],
        ["75", "47"],
        ["97", "75"],
        ["47", "61"],
        ["75", "61"],
        ["47", "29"],
        ["75", "13"],
        ["53", "13"],
    ]

    pages = [
        ["75", "47", "61", "53", "29"],
        ["97", "61", "53", "29", "13"],
        ["75", "29", "13"],
        ["75", "97", "47", "61", "53"],
        ["61", "13", "29"],
        ["97", "13", "75", "29", "47"],
    ]

    assert solve_part_1(rules, pages) == 143


def solve_part_2(rules, pages_list):
    sum = 0

    invalid_pages = []

    for pages in pages_list:
        eligible_rules = []
        for rule in rules:
            before, after = rule
            if before in pages and after in pages:
                eligible_rules.append(rule)

        valid = True
        for ix, page in enumerate(pages):
            for before, after in eligible_rules:
                if page == before and after in pages[:ix]:
                    valid = False
                    break
            if not valid:
                break

        if not valid:
            invalid_pages.append(pages)

    for pages in invalid_pages:
        eligible_rules = []
        for rule in rules:
            before, after = rule
            if before in pages and after in pages:
                eligible_rules.append(rule)

        befores = {}
        for e in eligible_rules:
            before, after = e
            if before not in befores:
                befores[before] = 0
            befores[before] += 1

        sorted_pages = sorted(pages, key=lambda k: -befores.get(k, 0))
        middle = sorted_pages[len(sorted_pages) // 2]
        sum += int(middle)

    return sum


if __name__ == "__main__":
    sample_rules, sample_pages = parse_input(read_input("05/sample.txt"))
    input_rules, input_pages = parse_input(read_input("05/input.txt"))

    print(f"part 1 sample {solve_part_1(sample_rules, sample_pages)}")
    print(f"part 1 input {solve_part_1(input_rules, input_pages)}")

    print(f"part 2 sample {solve_part_2(sample_rules, sample_pages)}")
    print(f"part 1 input {solve_part_2(input_rules, input_pages)}")

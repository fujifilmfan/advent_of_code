"""
Day 4: Ceres Search
===================
- cartesian product
- control flow
- grid search
"""
from itertools import product

sample = (
    "MMMSXXMASM\n"
    "MSAMXMSMSA\n"
    "AMXSXMAAMM\n"
    "MSAMASMSMX\n"
    "XMASAMXAMM\n"
    "XXAMMXXAMA\n"
    "SMSMSASXSS\n"
    "SAXAMASAAA\n"
    "MAMMMXMMMM\n"
    "MXMXAXMASX\n"
)

sample_lines = sample.split("\n")

lines = []
with open("day4_input.txt") as f:
    for line in f:
        lines.append(line.rstrip())

numbers = [-1, 0, 1]
relative_coordinates = list(product(numbers, repeat=2))
relative_coordinates.remove((0, 0))


def find_xmas(pos: tuple, direction: list, text: list) -> int:
    x, y = pos
    found_ms = []
    found_as = []
    found_ss = []
    line_length = len(text[0])
    for i, j in direction:
        if (
            x + (3 * i) < 0
            or x + (3 * i) >= line_length
            or y + (3 * j) < 0
            or y + (3 * j) >= line_length
        ):
            continue
        if text[x + i][y + j] == "M":
            found_ms.append((i, j))
    if found_ms:
        for i, j in found_ms:
            if text[x + (2 * i)][y + (2 * j)] == "A":
                found_as.append((i, j))
    if found_as:
        for i, j in found_as:
            if text[x + (3 * i)][y + (3 * j)] == "S":
                found_ss.append((i, j))

    return len(found_ss)


def count_xmas(puzzle_input: list):
    count = 0
    for line_num, puzzle_line in enumerate(puzzle_input):
        for char_num, char in enumerate(puzzle_line):
            cur_pos = (line_num, char_num)
            if char == "X":
                count += find_xmas(cur_pos, relative_coordinates, puzzle_input)

    return count


print(count_xmas(sample_lines))  # 2613 <-- correct (18 for the sample)

"""
S.S..S.M..M.S..M.M
.A....A....A....A.
M.M..S.M..M.S..S.S
"""
xmas_patterns = {
    "S": [
        [(1, 1, "A"), (2, 2, "M"), (0, 2, "S"), (2, 0, "M")],
        [(1, 1, "A"), (2, 2, "M"), (0, 2, "M"), (2, 0, "S")],
    ],
    "M": [
        [(1, 1, "A"), (2, 2, "S"), (0, 2, "S"), (2, 0, "M")],
        [(1, 1, "A"), (2, 2, "S"), (0, 2, "M"), (2, 0, "S")],
    ],
}


def find_x_shaped_mas(pos: tuple, letter: str, text: list) -> bool:
    x, y = pos
    line_length = len(text[0])
    if x + 2 >= line_length or y + 2 >= line_length:
        return False
    for pattern in xmas_patterns[letter]:
        found = True
        for i, j, char in pattern:
            if text[x + i][y + j] != char:
                found = False
                break
        if found:
            return True
    return False


def count_x_shaped_mas(puzzle_input: list):
    count = 0
    for line_num, puzzle_line in enumerate(puzzle_input):
        for char_num, char in enumerate(puzzle_line):
            cur_pos = (line_num, char_num)
            found = False
            if char == "S":
                found = find_x_shaped_mas(cur_pos, "S", puzzle_input)
            elif char == "M":
                found = find_x_shaped_mas(cur_pos, "M", puzzle_input)
            if found:
                count += 1

    return count


print(count_x_shaped_mas(lines))  # 1905 <-- correct (9 for the sample)

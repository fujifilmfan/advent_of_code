"""
Day 5: Print Queue
==================
- index of item in list
- set operations
- control flow
- while loops
"""

sample = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


puzzle_input = []
with open("day6_input.txt") as f:
    for line in f:
        puzzle_input.append(line.rstrip())

dirs = {
    0: (-1, 0),
    90: (0, 1),
    180: (1, 0),
    270: (0, -1),
}


def find_start(puzzle_map: list) -> tuple:
    for i, row in enumerate(puzzle_map):
        for j, col in enumerate(row):
            if col == "^":
                return i, j


def count_positions(puzzle_map: list[str]) -> int:
    map_width = len(puzzle_map[0])
    map_height = len(puzzle_map)
    y, x = find_start(puzzle_map)
    facing = 0
    guard_on_map = True
    positions = set()
    # print(puzzle_map)

    def step(cur_y, cur_x, direction):
        return cur_y + dirs[direction][0], cur_x + dirs[direction][1]

    while guard_on_map:
        positions.add((y, x))
        new_y, new_x = step(y, x, facing)
        if new_y < 0 or new_y >= map_height or new_x < 0 or new_x >= map_width:
            break
        if puzzle_map[new_y][new_x] == "#":
            facing = (facing + 90) % 360
        else:
            y, x = new_y, new_x

    for y, x in positions:
        puzzle_map[y] = puzzle_map[y][:x] + "X" + puzzle_map[y][x + 1 :]
    for row in puzzle_map:
        print(row)

    return len(positions)


print(find_start(sample))
print(count_positions(sample))  # 41

# Part 1
# print(count_positions(puzzle_input))  # 5162 <-- correct

# Part 2
# def insert_good_name(puzzle_map: list) -> int:
#     map_width = len(puzzle_map[0])
#     map_height = len(puzzle_map)
#     y, x = find_start(puzzle_map)
#     facing = 0
#     guard_on_map = True
#     positions = set()
#
#     def step(cur_y, cur_x, direction):
#         return cur_y + dirs[direction][0], cur_x + dirs[direction][1]
#
#     while guard_on_map:
#         positions.add((y, x))
#         new_y, new_x = step(y, x, facing)
#         if new_y < 0 or new_y >= map_height or new_x < 0 or new_x >= map_width:
#             break
#         if puzzle_map[new_y][new_x] == "#":
#             facing = (facing + 90) % 360
#         else:
#             y, x = new_y, new_x
#
#     return len(positions)

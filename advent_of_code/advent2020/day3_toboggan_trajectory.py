#!/usr/bin/env python
"""
From your starting position at the top-left, check the position that is
right 3 and down 1. Then, check the position that is right 3 and down 1
from there, and so on until you go past the bottom of the map.
"""

import argparse


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Optimal trajectory options')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a
                        plaintext file with each record on its own line.
                        """)
    return parser.parse_args(args)


def lines_from_file(path):
    lines = []
    with open(path) as handle:
        for line in handle:
            lines.append(line.rstrip('\n'))
    return lines


def main(args):
    cli_args = return_parsed_args(args)

    local_map = lines_from_file(cli_args.filename)

    paths = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    tree_counts = []
    for path in paths:
        tree_counts.append(count_trees(path, local_map))

    product = 1
    for tree_count in tree_counts:
        print(tree_count)
        product *= tree_count

    print(product)
    return product


def count_trees(path, local_map):
    right, down = path
    row_increment = down
    col_increment = right
    tot_rows = len(local_map)
    tot_cols = len(local_map[0])

    trees = 0
    while row_increment < tot_rows:
        col_increment = col_increment % tot_cols
        landscape = local_map[row_increment][col_increment]

        if landscape == '#':
            trees += 1

        row_increment += down
        col_increment += right
    return trees


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 237
# Part Two
# 2106818610 (65, 237, 59, 61, 38)

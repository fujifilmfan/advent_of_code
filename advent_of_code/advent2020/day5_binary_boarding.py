#!/usr/bin/env python
"""
As a sanity check, look through your list of boarding passes. What is
the highest seat ID on a boarding pass?

What is the ID of your seat?
"""

import argparse


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Valid password count')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a
                        plaintext file with each record on its own line.
                        """)
    return parser.parse_args(args)


def lines_from_file(path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def main(args):
    cli_args = return_parsed_args(args)
    path = cli_args.filename

    # highest = max(boarding_passes_from_file(path))
    seat_ids = []
    for seat_id in boarding_passes_from_file(path):
        seat_ids.append(seat_id)

    seat_ids.sort()

    my_seat = infer_my_seat(seat_ids)

    print(max(seat_ids))
    print(my_seat)

    return max(seat_ids), my_seat


def boarding_passes_from_file(path):
    boarding_passes = lines_from_file(path)
    yield from calculate_seat_id(boarding_passes)


def calculate_seat_id(boarding_passes):
    for boarding_pass in boarding_passes:
        rows = list(range(128))
        cols = list(range(8))

        row = determine_seat_row_or_col(boarding_pass[:7], rows)
        col = determine_seat_row_or_col(boarding_pass[7:], cols)

        yield (row * 8) + col


def determine_seat_row_or_col(boarding_pass_slice, num_range):
    num_range = num_range
    for _ in boarding_pass_slice:
        half = len(num_range) // 2
        if _ == 'F' or _ == 'L':
            num_range = num_range[:half]
        elif _ == 'B' or _ == 'R':
            num_range = num_range[half:]
    return num_range[0]


def infer_my_seat(seat_ids):
    possible_seats = range(1032)
    for seat in possible_seats[1:-1]:
        if seat not in seat_ids:
            if seat - 1 not in seat_ids:
                continue
            elif seat + 1 not in seat_ids:
                continue
            else:
                return seat


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# BBBFFBBLRL, 922
# Part Two
# 747

#!/usr/bin/env python
"""

Part 1: Count the number of times a depth measurement increases from
the previous measurement.
Part 2: Consider sums of a three-measurement sliding window. How many
sums are larger than the previous sum?
"""

import argparse


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Depth readings')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a
                        plaintext file with each record on its own line.
                        """)
    parser.add_argument('-w', '--window', type=int, default=1)
    return parser.parse_args(args)


def return_file_contents(path):
    """Open specified file and return lines as items in a list"""
    file_contents = []
    with open(path) as input_file:
        for line in input_file:
            file_contents.append(int(line))
    return file_contents


def main(args):
    cli_args = return_parsed_args(args)
    depths = return_file_contents(cli_args.filename)
    look_ahead = cli_args.window

    increases = 0
    i = 0

    while i < len(depths)-look_ahead:
        try:
            sum1 = sum([depths[i + _] for _ in range(look_ahead)])
            sum2 = sum([depths[i + _ + 1] for _ in range(look_ahead)])
        except IndexError:
            break
        else:
            if sum2 > sum1:
                increases += 1
            i += 1

    print(f"Number of increases for {look_ahead}-item window: {increases}")
    return increases


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 1564
# Part Two
# 1611

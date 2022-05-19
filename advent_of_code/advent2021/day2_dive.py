#!/usr/bin/env python
"""

Part 1: Determine your horizontal and vertical position and multiply the
results.
Part 2:

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
    parser.add_argument('-a', '--aim', type=bool, default=False)
    return parser.parse_args(args)


def return_file_contents(path):
    """Open specified file and return lines as items in a list"""
    with open(path) as input_file:
        for line in input_file:
            yield line


def main(args):
    cli_args = return_parsed_args(args)
    instructions = return_file_contents(cli_args.filename)
    aim = cli_args.aim

    a = 0
    h = 0
    v = 0

    if aim is False:
        for instruction in instructions:
            direction, amount = instruction.split()
            if direction == 'forward':
                h += int(amount)
            elif direction == 'down':
                v += int(amount)
            elif direction == 'up':
                v -= int(amount)
        print(h*v)
        return h * v
    else:
        for instruction in instructions:
            direction, amount = instruction.split()
            if direction == 'forward':
                h += int(amount)
                v += a * int(amount)
            elif direction == 'down':
                a += int(amount)
            elif direction == 'up':
                a -= int(amount)
        print(h*v)
        return h * v


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 1936494
# Part Two
# 1997106066

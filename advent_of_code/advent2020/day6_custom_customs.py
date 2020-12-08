#!/usr/bin/env python
"""
Another group asks for your help, then another, and eventually you've
collected answers from every group on the plane (your puzzle input).
Each group's answers are separated by a blank line, and within each
group, each person's answers are on a single line.

For each group, count the number of questions to which anyone answered
"yes". What is the sum of those counts?
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

    total = sum(customs_responses_from_file(path))

    print(total)
    return total


def customs_responses_from_file(path):
    customs_responses = lines_from_file(path)
    yield from count_yeses(customs_responses)


def count_yeses(customs_responses):
    seen = set()
    for response in customs_responses:
        if response == '':
            yield len(seen)
            seen = set()
            continue
        resp_set = set(response)
        seen.update(resp_set)
    yield len(seen)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 6778
# Part Two
#

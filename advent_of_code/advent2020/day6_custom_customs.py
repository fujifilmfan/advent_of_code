#!/usr/bin/env python
"""
Another group_response asks for your help, then another, and eventually you've
collected answers from every group_response on the plane (your puzzle input).
Each group_response's answers are separated by a blank line, and within each
group_response, each person's answers are on a single line.

Part 1
For each group_response, count the number of questions to which anyone answered
"yes". What is the sum of those counts?

Part 2
For each group_response, count the number of questions to which everyone
answered "yes". What is the sum of those counts?
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
    """Yield lines from a file.

    :param path: STR; path to input file
    :return: OBJ; generator
    """
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def main(args):
    cli_args = return_parsed_args(args)
    path = cli_args.filename

    groups = customs_responses_from_file(path)
    yeses = 0
    group_yeses = 0

    for group in groups:
        yeses += count_yeses(group)
        group_yeses += count_group_yeses(group)

    print(yeses)
    print(group_yeses)


def customs_responses_from_file(path):
    """Read lines from file and yield group responses from input file.

    :param path: STR; path to input file
    :return: OBJ; generator
    """

    customs_responses = lines_from_file(path)
    yield from group_response(customs_responses)


def group_response(customs_responses):
    """Yield group_response from the customs_responses input.

    :param customs_responses: OBJ; generator
    :return: OBJ; generator
    """
    group_resp = []
    for response in customs_responses:
        if response == '':
            yield group_resp
            group_resp = []
            continue
        group_resp.append(response)
    yield group_resp


def count_yeses(group):
    """Count the number of questions to which anyone answered "yes".

    :param group: OBJ; generator
    :return: INT
    """
    seen = set()
    for resp in group:
        resp_set = set(resp)
        seen.update(resp_set)
    return len(seen)


def count_group_yeses(group):
    """Count the number of questions to which everyone answered "yes".

    :param group: OBJ; generator
    :return: INT
    """
    universal = set(group[0])
    for resp in group[1:]:
        universal.intersection_update(set(resp))
    return len(universal)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 6778
# Part Two
# 3406

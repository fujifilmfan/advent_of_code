#!/usr/bin/env python
"""
Part 1
What is the first number that is not the sum of two of the previous
25 numbers before it?

Part 2
What is the encryption weakness in your XMAS-encrypted list of numbers?
"""

import argparse
from itertools import combinations


def parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='eXchange-Masking Addition System options')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a 
                        plaintext file with each record on its own line.
                        """)
    parser.add_argument('-p', '--preamble', type=int, default=25, help="""
                        Optional. Enter the length of the preamble that the 
                        decoder should use. This is essentially the reading 
                        frame.
                        """)
    return parser.parse_args(args)


def lines_from_file(path):
    """Return lines from a file.

    :param path: STR; path to input file
    :return: OBJ; generator
    """

    file_contents = []
    with open(path) as handle:
        for line in handle:
            file_contents.append(int(line.rstrip('\n')))
    return file_contents


def main(args):
    cli_args = parsed_args(args)
    path = cli_args.filename
    preamble_len = cli_args.preamble

    xmas_data = lines_from_file(path)
    outlier = find_outlier(xmas_data, preamble_len)

    contiguous_summands = find_contiguous(xmas_data, outlier)
    solution = min(contiguous_summands) + max(contiguous_summands)

    print(solution)
    return solution


def find_outlier(xmas_data, preamble_len):
    """Find the first number in the data that is not the sum of the
    previous x numbers, where x is preamble_len.

    :param xmas_data: LIST; ints of the XMAS encoded data
    :param preamble_len: INT; reading frame
    :return: INT; the first number in the data that is not the sum of
        the previous preamble_len numbers
    """

    start_i = 0
    end_i = preamble_len

    while end_i < len(xmas_data):
        result = find_summands(xmas_data[start_i:end_i], xmas_data[end_i])
        if result is not True:
            return result
        start_i += 1
        end_i += 1


def find_summands(preamble, sum_):
    """Find two numbers in preamble that add to sum_.
    
    :param preamble: LIST; ints of the XMAS encoded data (partial list)
    :param sum_: INT; the first number in the data that is not the sum
        of the previous preamble_len numbers
    :return: INT or True; original sum_ if two summands are not found,
        True if they are
    """

    resp = sum_
    for num1, num2 in combinations(preamble, 2):
        if num1 > sum_ or num2 > sum_:
            continue
        if num1 + num2 == sum_:
            resp = True
            break
    return resp


def find_contiguous(xmas_data, sum_):
    """Find contiguous numbers in data that add to sum_.

    :param xmas_data: LIST; ints of the XMAS encoded data
    :param sum_: INT; the first number in the data that is not the sum
        of the previous preamble_len numbers
    :return: LIST; section of contiguous xmas_data that sums to sum_
    """

    start_i = 0
    increment = 0
    total = 0

    while total < sum_:
        total += xmas_data[start_i + increment]
        if total > sum_:
            start_i += 1
            increment = 0
            total = 0
            continue
        elif total == sum_:
            return xmas_data[start_i:start_i+increment+1]
        increment += 1


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 1639024365
# Part Two
# 219202240

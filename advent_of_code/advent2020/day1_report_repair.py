#!/usr/bin/env python

import argparse

SUM = 2020


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Report repair solution options')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a
                        plaintext file with each record on its own line.
                        """)
    parser.add_argument('-s', '--summands', type=int, help="""
                        Use this argument to determine the number of 
                        expenses that add to the target sum. Currently, 
                        2 and 3 are supported.
                        """)
    return parser.parse_args(args)


def lines_from_file(path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def main(args):
    cli_args = return_parsed_args(args)
    expenses = lines_from_file(cli_args.filename)
    num_summands = cli_args.summands
    product = 1
    summands = find_summands(SUM, num_summands, expenses)
    if summands is not None:
        for summand in summands:
            product *= summand

    print(product)
    return product


def find_summands(target, num_summands, expenses):

    for expense in expenses:
        # Shorten the list so we're only looking ahead.
        expenses = expenses[1:]
        diff = target - expense

        if num_summands == 2 and diff in expenses:
            return diff, expense
        elif num_summands > 2:
            if num_summands-1 <= len(expenses):
                summands = find_summands(diff, num_summands-1, expenses)
                if summands is not None:
                    return summands + (expense, )


# Previous version
# def find_summands(sum_, num_summands, expenses):
#     if num_summands > 2:
#         summands = None
#         for num, expense in enumerate(expenses):
#             if num_summands-1 <= len(expenses[num+1:]):
#                 summands = find_summands(
#                     sum_-expense, num_summands-1, expenses[num+1:])
#             if summands is None:
#                 continue
#             else:
#                 return summands + (expense,)
#     elif num_summands == 2:
#         skip = {'greatest': sum_ - min(expenses), 'least': sum_ - max(expenses)}
#         for num, expense in enumerate(expenses):
#             if skip['least'] > expense > skip['greatest']:
#                 continue
#             if sum_ - expense in expenses[num+1:]:
#                 return expense, sum_-expense
#             continue


# Partly working generator version (only 2 summands)
# def find_summands(sum_, num_summands, expenses):
#     if num_summands > 2:
#         for expense in expenses:
#             seen.append(expense)
#             summands = find_summands(
#                 sum_-expense, num_summands-1, expenses)
#             if summands is None:
#                 continue
#             else:
#                 return summands + (expense,)
#     elif num_summands == 2:
#         for expense in expenses:
#             seen.append(expense)
#             if sum_ - expense in seen:
#                 return expense, sum_-expense
#             # continue


# Original functions
def find_sum_from_two(sum_, expenses):
    skip = {'greatest': sum_ - min(expenses), 'least': sum_ - max(expenses)}
    for num, expense in enumerate(expenses):
        if skip['least'] > expense > skip['greatest']:
            continue
        if sum_ - expense in expenses[num+1:]:
            return expense, sum_-expense
        continue


def find_sum_from_three(sum_, expenses):
    for num, expense in enumerate(expenses):
        summands = find_sum_from_two(sum_-expense, expenses[num+1:])
        if summands is None:
            continue
        else:
            return summands + (expense,)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 545379
# Part Two
# 257778836 (973, 428, 619)

#!/usr/bin/env python
"""
To try to debug the problem, they have created a list (your puzzle
input) of passwords (according to the corrupted database) and the
corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password
policy indicates the lowest and highest number of times a given letter
must appear for the password to be valid. For example, 1-3 a means that
the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password,
cdefg, is not; it contains no instances of b, but needs at least 1. The
first and third passwords are valid: they contain one a or nine c, both
within the limits of their respective policies.

How many passwords are valid according to their policies?
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
    parser.add_argument('-s', '--sled', action='store_true', help="""
                        Use this argument to evaluate passwords using 
                        the sled rental place policy instead of the 
                        Official Toboggan Corporate Policy.
                        """)
    return parser.parse_args(args)


def main(args):
    cli_args = return_parsed_args(args)
    lines = lines_from_file(cli_args.filename)
    policy_passwords = password_entry(lines)

    valid_pwds = 0
    for policy_pwd in policy_passwords:
        if cli_args.sled is True:
            if evaluate_sled_policy(policy_pwd) is True:
                valid_pwds += 1
        else:
            if evaluate_toboggan_policy(policy_pwd) is True:
                valid_pwds += 1

    print(valid_pwds)
    return valid_pwds


def lines_from_file(path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def password_entry(lines):
    for line in lines:
        span, char, pwd = line.split(' ')
        num1, num2 = span.split('-')
        char = char.rstrip(':')
        yield (int(num1), int(num2)), char, pwd


def evaluate_sled_policy(policy_password):
    (min_, max_), char, pwd = policy_password
    return True if min_ <= pwd.count(char) <= max_ else False


def evaluate_toboggan_policy(policy_password):
    (pos1, pos2), char, pwd = policy_password
    if pwd[pos1-1] == char and pwd[pos2-1] == char:
        return False
    elif pwd[pos1-1] != char and pwd[pos2-1] != char:
        return False
    return True


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 439
# Part Two
# 584

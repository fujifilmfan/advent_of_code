#!/usr/bin/env python

# import argparse

password_input_range = '138307-654504'
password_min = 138307
password_max = 654504


def count_valid_passwords(min_, max_):

    count = 0
    passwords = []
    current_password = min_

    while current_password <= max_:
        if password_has_a_double(str(current_password)):
            if password_has_increasing_digits(str(current_password)):
                count += 1
                passwords.append(current_password)
        current_password += 1

    return count, passwords


def password_has_a_double(num):
    """

    :param num: STR; represents a six-digit integer
    :return: BOOL
    """

    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            return True
    return False


def password_has_increasing_digits(num):
    """

    :param num: STR; represents a six-digit integer
    :return: BOOL
    """

    for i in range(len(num)-1):
        if num[i] > num[i+1]:
            return False
    return True


def password_double_is_isolated(possible_passwords):

    total_count = 0

    for num in possible_passwords:
        count = 0
        num = str(num)
        repeats = 1
        for i in range(len(num)-1):
            if num[i] == num[i+1]:
                repeats += 1
            else:
                if repeats > 2:
                    repeats = 1
                elif repeats == 2:
                    count = 1
        if repeats == 2:
            count = 1

        if count == 1:
            total_count += 1

    return total_count


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(
    #     description='Password solution options.')
    #
    # parser.add_argument('num', type=list)
    # parser.add_argument('read_file_name', type=str, help="""
    #                     Required. Enter the path to the input file that you
    #                     would like to analyze.  The file should be a
    #                     plaintext file with each record on its own line.
    #                     """)
    # args = parser.parse_args()
    results = count_valid_passwords(password_min, password_max)
    print(results[0])
    narrowed_results = password_double_is_isolated(results[1])
    print(narrowed_results)

# Part One:
# 1855
# Part Two:
# 1253

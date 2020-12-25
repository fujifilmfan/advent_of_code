#!/usr/bin/env python
"""
Due to some questionable network security, you realize you might be
able to solve both of these problems at the same time.
[Haha!]

"""

import argparse
import re


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Passport processing options')
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

    rules = {
        'required_fields': ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'],
        'optional_fields': ['cid'],
        'byr': {
            'digits': 4,
            'least': 1920,
            'most': 2002,
            'regex': re.compile('^(19[2-9][0-9]|200[0-2])$')
        },
        'iyr': {
            'digits': 4,
            'least': 2010,
            'most': 2020,
            'regex': re.compile('^(201[0-9]|2020)$')
        },
        'eyr': {
            'digits': 4,
            'least': 2020,
            'most': 2030,
            'regex': re.compile('^(202[0-9]|2030)$')
        },
        'hgt': {
            'cm': {
                'least': 150,
                'most': 193,
            },
            'in': {
                'least': 59,
                'most': 76,
            },
            'regex': re.compile(
                '^(59in|6[0-9]in|7[0-6]in|1[5-8][0-9]cm|19[0-3]cm)$')
        },
        'hcl': {
            'regex': re.compile('^(#[0-9a-f]{6})$')
        },
        'ecl': {
            'allowed': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
            'regex': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
        },
        'pid': {
            'digits': 9,
            'regex': re.compile('^([0-9]{9})$')
        },
        'cid': '',
    }

    valid_passport_count = 0
    for passport in passport_records_from_file(cli_args.filename):
        if valid_passport(passport, rules):
            valid_passport_count += 1

    print(valid_passport_count)
    return valid_passport_count


def passport_records_from_file(path):
    lines = lines_from_file(path)
    yield from passport_records(lines)


def passport_records(lines):
    """Create a passport dict for each entry in the input file."""

    record = {}
    for line in lines:
        if line == '':
            yield record
            record = {}
            continue
        fields = line.split(' ')
        for field in fields:
            key, value = field.split(':')
            record[key] = value
    yield record


def valid_passport(passport, rules):
    for field in rules['required_fields']:
        if field not in passport.keys():
            return False
    if rules['byr']['regex'].match(passport['byr']) is None:
        return False
    if rules['iyr']['regex'].match(passport['iyr']) is None:
        return False
    if rules['eyr']['regex'].match(passport['eyr']) is None:
        return False
    if rules['hgt']['regex'].match(passport['hgt']) is None:
        return False
    if rules['hcl']['regex'].match(passport['hcl']) is None:
        return False
    if rules['ecl']['regex'].match(passport['ecl']) is None:
        return False
    if rules['pid']['regex'].match(passport['pid']) is None:
        return False
    return True


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 239 (out of 295 passports)
# Part Two
# 188

#!/usr/bin/env python

import re

import pytest

from advent_of_code.advent2020 import day4_passport_processing as day4

_MODULE = 'advent_of_code.advent2020.day4_passport_processing'

FOUR_PASSPORTS = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in',
]
PASSPORT_1 = {
    'ecl': 'gry',
    'pid': '860033327',
    'eyr': '2020',
    'hcl': '#fffffd',
    'byr': '1937',
    'iyr': '2017',
    'cid': '147',
    'hgt': '183cm',
}
PASSPORT_2 = {
    'iyr': '2013',
    'ecl': 'amb',
    'cid': '350',
    'eyr': '2023',
    'pid': '028048884',
    'hcl': '#cfa07d',
    'byr': '1929',
}
PASSPORT_3 = {
    'hcl': '#ae17e1',
    'iyr': '2013',
    'eyr': '2024',
    'ecl': 'brn',
    'pid': '760753108',
    'byr': '1931',
    'hgt': '179cm',
}
PASSPORT_4 = {
    'hcl': '#cfa07d',
    'eyr': '2025',
    'pid': '166559648',
    'iyr': '2011',
    'ecl': 'brn',
    'hgt': '59in',
}

INVALID_PASSPORTS = [
    'eyr:1972 cid:100',
    'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
    '',
    'iyr:2019',
    'hcl:#602927 eyr:1967 hgt:170cm',
    'ecl:grn pid:012533040 byr:1946',
    '',
    'hcl:dab227 iyr:2012',
    'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
    '',
    'hgt:59cm ecl:zzz',
    'eyr:2038 hcl:74454a iyr:2023',
    'pid:3556412378 byr:2007',
]
INVALID_PPT_1 = {
    'eyr': '1972',
    'cid': '100',
    'hcl': '#18171d',
    'ecl': 'amb',
    'hgt': '170',
    'pid': '186cm',
    'iyr': '2018',
    'byr': '1926',
}
INVALID_PPT_2 = {
    'iyr': '2019',
    'hcl': '#602927',
    'eyr': '1967',
    'hgt': '170cm',
    'ecl': 'grn',
    'pid': '012533040',
    'byr': '1946',
}
INVALID_PPT_3 = {
    'hcl': 'dab227',
    'iyr': '2012',
    'ecl': 'brn',
    'hgt': '182cm',
    'pid': '021572410',
    'eyr': '2020',
    'byr': '1992',
    'cid': '277',
}
INVALID_PPT_4 = {
    'hgt': '59cm',
    'ecl': 'zzz',
    'eyr': '2038',
    'hcl': '74454a',
    'iyr': '2023',
    'pid': '3556412378',
    'byr': '2007',
}

VALID_PASSPORTS = [
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
    'hcl:#623a2f',
    '',
    'eyr:2029 ecl:blu cid:129 byr:1989',
    'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
    '',
    'hcl:#888785',
    'hgt:164cm byr:2001 iyr:2015 cid:88',
    'pid:545766238 ecl:hzl',
    'eyr:2022',
    '',
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
]
VALID_PPT_1 = {
    'pid': '087499704',
    'hgt': '74in',
    'ecl': 'grn',
    'iyr': '2012',
    'eyr': '2030',
    'byr': '1980',
    'hcl': '#623a2f',
}
VALID_PPT_2 = {
    'eyr': '2029',
    'ecl': 'blu',
    'cid': '129',
    'byr': '1989',
    'iyr': '2014',
    'pid': '896056539',
    'hcl': '#a97842',
    'hgt': '165cm',
}
VALID_PPT_3 = {
    'hcl': '#888785',
    'hgt': '164cm',
    'byr': '2001',
    'iyr': '2015',
    'cid': '88',
    'pid': '545766238',
    'ecl': 'hzl',
    'eyr': '2022',
}
VALID_PPT_4 = {
    'iyr': '2010',
    'hgt': '158cm',
    'hcl': '#b6652a',
    'ecl': 'blu',
    'byr': '1944',
    'eyr': '2021',
    'pid': '093154719',
}

RULES = {
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


def test_passport_records():
    """Test day4_passport_processing.passport_records.

    The passport_records function returns a generator, so we'll make
    four assertions to test the output instead of using parametrize.

    :return: None
    """

    # Act
    actual = day4.passport_records(FOUR_PASSPORTS)

    # Assert
    assert next(actual) == PASSPORT_1
    assert next(actual) == PASSPORT_2
    assert next(actual) == PASSPORT_3
    assert next(actual) == PASSPORT_4


@pytest.mark.parametrize('passport, expected', [
    (PASSPORT_1, True),
    (PASSPORT_2, False),
    (PASSPORT_3, True),
    (PASSPORT_4, False),
    (INVALID_PPT_1, False),
    (INVALID_PPT_2, False),
    (INVALID_PPT_3, False),
    (INVALID_PPT_4, False),
    (VALID_PPT_1, True),
    (VALID_PPT_2, True),
    (VALID_PPT_3, True),
    (VALID_PPT_4, True),
])
def test_valid_passport(passport, expected):
    """Test day4_passport_processing.valid_passport.

    :param passport: DICT
    :param expected: BOOL
    :return: None
    """

    # Arrange

    # Act
    actual = day4.valid_passport(passport, RULES)

    # Assert
    assert actual == expected



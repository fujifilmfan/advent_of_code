#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day2_password_philosophy as pwd_phil

_MODULE = 'advent_of_code.advent2020.day2_password_philosophy'


@pytest.mark.parametrize('entry, expected', [
    (((1, 3), 'a', 'abcde'), True),
    (((1, 3), 'b', 'cdefg'), False),
    (((2, 9), 'c', 'ccccccccc'), True),
])
def test_evaluate_sled_policy(entry, expected):

    # Arrange

    # Act
    actual = pwd_phil.evaluate_sled_policy(entry)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('entry, expected', [
    (((1, 3), 'a', 'abcde'), True),
    (((1, 3), 'b', 'cdefg'), False),
    (((2, 9), 'c', 'ccccccccc'), False),
])
def test_evaluate_toboggan_policy(entry, expected):

    # Arrange

    # Act
    actual = pwd_phil.evaluate_toboggan_policy(entry)

    # Assert
    assert actual == expected


def test_password_entry():

    # Arrange
    entry = ['10-20 d: djddddccdbdddddddndd']
    expected = ((10, 20), 'd', 'djddddccdbdddddddndd')

    # Act
    actual = next(pwd_phil.password_entry(entry))

    # Assert
    assert actual == expected


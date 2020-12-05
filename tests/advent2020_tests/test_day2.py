#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day2_password_philosophy as day2

_MODULE = 'advent_of_code.advent2020.day2_password_philosophy'


@pytest.mark.parametrize('entry, expected', [
    (((1, 3), 'a', 'abcde'), True),
    (((1, 3), 'b', 'cdefg'), False),
    (((2, 9), 'c', 'ccccccccc'), True),
])
def test_evaluate_sled_policy(entry, expected):
    """Test day2_password_philosophy.evaluate_sled_policy.

    :param entry: TUPLE; policies and passwords
    :param expected: BOOL; does the password satisfy the policy?
    :return: None
    """

    # Arrange

    # Act
    actual = day2.evaluate_sled_policy(entry)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('entry, expected', [
    (((1, 3), 'a', 'abcde'), True),
    (((1, 3), 'b', 'cdefg'), False),
    (((2, 9), 'c', 'ccccccccc'), False),
])
def test_evaluate_toboggan_policy(entry, expected):
    """Test day2_password_philosophy.evaluate_toboggan_policy.

    :param entry: TUPLE; policies and passwords
    :param expected: BOOL; does the password satisfy the policy?
    :return: None
    """

    # Arrange

    # Act
    actual = day2.evaluate_toboggan_policy(entry)

    # Assert
    assert actual == expected


def test_password_entry():
    """Test day2_password_philosophy.password_entry."""

    # Arrange
    entry = ['10-20 d: djddddccdbdddddddndd']
    expected = ((10, 20), 'd', 'djddddccdbdddddddndd')

    # Act
    actual = next(day2.password_entry(entry))

    # Assert
    assert actual == expected

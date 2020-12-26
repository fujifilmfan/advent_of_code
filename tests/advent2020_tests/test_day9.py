#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day9_encoding_error as day9

_MODULE = 'advent_of_code.advent2020.day9_encoding_error'

XMAS_DATA = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_find_outlier():
    """Test day9_encoding_error.find_outlier.

    This is not a proper unit test as the function calls another
    function repeatedly.

    return: None
    """

    # Arrange
    expected = 127

    # Act
    actual = day9.find_outlier(XMAS_DATA, 5)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('preamble, sum_, expected', [
    ([35, 20, 15, 25, 47], 40, True),
    ([95, 102, 117, 150, 182], 127, 127),
])
def test_find_summands(preamble, sum_, expected):
    """ Test day9_encoding_error.find_summands.

    :param preamble: LIST; ints in the code
    :param sum_: INT
    :param expected: INT or True
    :return: None
    """

    # Arrange

    # Act
    actual = day9.find_summands(preamble, sum_)

    # Assert
    assert actual == expected


def test_find_contiguous():
    """ Test day9_encoding_error.find_contiguous.

    :return: None
    """

    # Arrange
    sum_ = 127
    expected = [15, 25, 47, 40]

    # Act
    actual = day9.find_contiguous(XMAS_DATA, sum_)

    # Assert
    assert actual == expected

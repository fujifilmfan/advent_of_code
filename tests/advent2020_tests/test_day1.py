#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day1_report_repair as day1

_MODULE = 'advent_of_code.advent2020.day1_report_repair'
SUM = 2020


@pytest.mark.parametrize('num, input_, expected', [
    (2, [2021, 1901, 979, 366, 299, 675, 1721, 1456], (1721, 299)),
    (3, [123, 366, 299, 979, 1721, 1456, 675], (675, 979, 366)),
    (2, [1, 2], None),
    (3, [503, 504, 506, 507], None),
    (4, [123, 503, 504, 506, 507], (507, 506, 504, 503)),
])
def test_find_summands(num, input_, expected):
    """Test day1_report_repair.find_summands.

    :param num: INT; number of summands needed to produce sum
    :param input_: LIST; integers
    :param expected: TUPLE; integers or None
    :return: None
    """

    # Act
    actual = day1.find_summands(SUM, num, input_)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('input_, expected', [
    ([2021, 1901, 979, 366, 299, 675, 1721, 1456], (299, 1721)),
    ([1, 2], None),
])
def test_find_sum_from_two(input_, expected):
    """Test day1_report_repair.find_sum_from_two.

    :param input_: LIST; integers
    :param expected: LIST; two integers or None
    :return: None
    """

    # Act
    actual = day1.find_sum_from_two(SUM, input_)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('input_, return_val, expected', [
    ([366, 299, 979, 1721, 1456, 675], (675, 979), (675, 979, 366)),
    ([1, 2], None, None),
])
def test_find_sum_from_three(input_, return_val, expected, mocker):
    """Test day1_report_repair.find_sum_from_three.

    :param input_: LIST; integers
    :param return_val: LIST; two integers from find_sum_from_two
    :param expected: LIST; two integers or None
    :param mocker: OBJ
    :return: None
    """

    # Act
    mocker.patch(f'{_MODULE}.find_sum_from_two', return_value=return_val)
    actual = day1.find_sum_from_three(SUM, input_)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('summands, expected', [
    ((299, 1721), 514579),
    ((428, 619, 973), 257778836),
    (None, 1),
])
def test_main(summands, expected, mocker):
    """Test day1_report_repair.main.

    :param summands: TUPLE; integers to be multiplied
    :param expected: INT; product of the two summands
    :param mocker: OBJ
    :return: None
    """

    # Arrange
    mocker.patch(f'{_MODULE}.return_parsed_args')
    mocker.patch(f'{_MODULE}.lines_from_file')
    mocker.patch(f'{_MODULE}.find_summands', return_value=summands)

    # Act
    actual = day1.main(None)

    # Assert
    assert actual == expected

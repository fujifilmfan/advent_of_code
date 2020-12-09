#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day5_binary_boarding as day5

_MODULE = 'advent_of_code.advent2020.day5_binary_boarding'
ROWS = list(range(128))
COLS = list(range(8))


@pytest.mark.parametrize('side_effects, expected', [
    ([1, 1], 9),
    ([1, 8], 16),
    ([63, 5], 509),
    ([64, 5], 517),
    ([127, 8], 1024),
])
def test_calculate_seat_id(side_effects, expected, mocker):
    """Test day5_binary_boarding.calculate_seat_id.

    :side_effects: LIST; INTs returned from determine_seat_row_or_col()
    :expected: INT; seat ID
    :return: None
    """

    # Arrange
    boarding_passes = ['any_iterable']
    mocker.patch(
        f'{_MODULE}.determine_seat_row_or_col', side_effect=side_effects)

    # Act
    actual = day5.calculate_seat_id(boarding_passes)

    # Assert
    assert next(actual) == expected


@pytest.mark.parametrize('boarding_pass_slice, num_range, expected', [
    ('FBFBBFF', ROWS, 44),
    ('RLR', COLS, 5),
    ('BFFFBBF', ROWS, 70),
    ('RRR', COLS, 7),
    ('FFFBBBF', ROWS, 14),
    ('BBFFBBF', ROWS, 102),
    ('RLL', COLS, 4),
])
def test_determine_seat_row_or_col(boarding_pass_slice, num_range, expected):
    """Test day5_binary_boarding.determine_seat_row_or_col.

    :boarding_pass_slice: STR
    :num_range: LIST; list of ints
    :expected: INT; row or column number
    :return: None
    """

    # Act
    actual = day5.determine_seat_row_or_col(boarding_pass_slice, num_range)

    # Assert
    assert actual == expected


def test_infer_my_seat():
    """Test day5_binary_boarding.infer_my_seat."""

    # Arrange
    seat_ids = [4, 5, 6, 8, 9, 10]
    expected = 7

    # Act
    actual = day5.infer_my_seat(seat_ids)

    # Assert
    assert actual == expected

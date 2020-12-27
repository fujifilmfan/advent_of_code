#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day10_adapter_array as day10

_MODULE = 'advent_of_code.advent2020.day10_adapter_array'


ADAPTER_SET1 = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
ADAPTER_SET2 = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19,
                20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39,
                42, 45, 46, 47, 48, 49, 52]
SET1_ANCHORS = {0: 0, 1: 1, 2: 4, 5: 7, 6: 10, 8: 12, 9: 15, 10: 16,
                11: 19, 12: 22}
SET2_ANCHORS = {0: 0, 4: 4, 5: 7, 9: 11, 10: 14, 11: 17, 14: 20,
                15: 23, 17: 25, 18: 28, 19: 31, 23: 35, 24: 38, 25: 39,
                26: 42, 27: 45, 31: 49, 32: 52}
SET1_ANCHOR_INDICES = [0, 1, 2, 5, 6, 8, 9, 10, 11, 12]
SET2_ANCHOR_INDICES = [0, 4, 5, 9, 10, 11, 14, 15, 17, 18, 19, 23, 24,
                       25, 26, 27, 31, 32]
SET1_GAPS = {
    'optional': [2, 1],
    'required': [],
}
SET2_GAPS = {
    'optional': [2, 1],
    'required': [3, 3, 3, 3],
}


@pytest.mark.parametrize('adapters, expected', [
    (ADAPTER_SET1, {1: 7, 3: 5}),
    (ADAPTER_SET2, {1: 22, 3: 10}),
])
def test_joltage_diff_distribution(adapters, expected):
    """Test day10_adapter_array.joltage_diff_distribution.

    :param adapters: LIST; adapter joltage ratings, previously sorted
    :param expected: DICT; joltage difference distribution; note that
        the difference can only be 1, 2, or 3
    :return: None
    """

    # Act
    actual = day10.joltage_diff_distribution(adapters)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('adapters, expected', [
    (ADAPTER_SET1, SET1_ANCHOR_INDICES),
    (ADAPTER_SET2, SET2_ANCHOR_INDICES),
])
def test_anchor_adapter_indices(adapters, expected):
    """Test day10_adapter_array.anchor_adapter_indices.

    :param adapters: LIST; adapter joltage ratings, previously sorted
    :param expected: LIST, ints representing indices of adapter ratings
        that cannot be removed from the chain
    :return:
    """

    # Act
    actual = day10.anchor_adapter_indices(adapters)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('indices, expected', [
    (SET1_ANCHOR_INDICES, SET1_GAPS),
    (SET2_ANCHOR_INDICES, SET2_GAPS),
])
def test_identify_optional_and_required_adapters(indices, expected):
    """Test day10_adapter_array.identify_optional_and_required_adapters.

    :param indices: LIST, ints representing indices of adapter ratings
        that cannot be removed from the chain
    :param expected: DICT; numbers of numbers that can fill gaps
        between anchors
    :return: None
    """

    # Act
    actual = day10.identify_optional_and_required_adapters(indices)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('gaps, expected', [
    (SET1_GAPS, 8),
    (SET2_GAPS, 19208),
])
def test_calculate_arrangements(gaps, expected):
    """Test day10_adapter_array.calculate_arrangements.

    :param expected: DICT; numbers of numbers that can fill gaps
        between anchors
    :param expected: INT; number of arrangements
    :return:
    """

    # Act
    actual = day10.calculate_arrangements(gaps)

    # Assert
    assert actual == expected

#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day6_custom_customs as day6

_MODULE = 'advent_of_code.advent2020.day6_custom_customs'


def test_group_response():
    """Test day6_custom_customs.group_response.

    :return: None
    """
    # Arrange
    customs_responses = ['abc', '', 'a', 'b', 'c']
    expected1 = ['abc']
    expected2 = ['a', 'b', 'c']

    # Act
    actual = day6.group_response(customs_responses)

    # Assert
    assert next(actual) == expected1
    assert next(actual) == expected2


@pytest.mark.parametrize('group, expected', [
    ('abc', 3),
    ('abac', 3),
    ('aaaa', 1),
    ('b', 1),
])
def test_count_yeses(group, expected):
    """Test day6_custom_customs.count_yeses.

    :param group: LIST
    :param expected: INT
    :return: None
    """

    # Act
    actual = day6.count_yeses(group)

    # Assert
    assert actual == expected


@pytest.mark.parametrize('group, expected', [
    (['abc'], 3),
    (['a', 'b', 'c'], 0),
    (['ab', 'ac'], 1),
    (['a', 'a', 'a', 'a'], 1),
    (['b'], 1),
])
def test_count_group_yeses(group, expected):
    """Test day6_custom_customs.count_group.yeses.

    :param group: LIST
    :param expected: INT
    :return: None
    """

    # Arrange
    # groups = '\n\nab\nac\n\na\na\na\na\n\nb'
    # expected = 6

    # Act
    actual = day6.count_group_yeses(group)

    # Assert
    assert actual == expected

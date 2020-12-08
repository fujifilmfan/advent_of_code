#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day6_custom_customs as day6

_MODULE = 'advent_of_code.advent2020.day6_custom_customs'


@pytest.mark.parametrize('group, expected', [
    ('abc', 3),
    ('abac', 3),
    ('aaaa', 1),
    ('b', 1),
])
def test_count_yeses(group, expected):

    # Act
    actual = day6.count_yeses(group)

    # Assert
    assert next(actual) == expected

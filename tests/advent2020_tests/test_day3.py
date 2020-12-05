#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day3_toboggan_trajectory as day3

_MODULE = 'advent_of_code.advent2020.day3_toboggan_trajectory'


@pytest.mark.parametrize('path, expected', [
    ((1, 1), 2), ((3, 1), 7), ((5, 1), 3), ((7, 1), 4), ((1, 2), 2)
])
def test_count_trees(path, expected):
    """Test day3_toboggan_trajectory.count_trees.

    :param path: TUPLE; amount to move right and down, respectively
    :param expected: INT; tree count
    :return: None
    """

    # Arrange
    local_map = [
        '..##.......',
        '#...#...#..',
        '.#....#..#.',
        '..#.#...#.#',
        '.#...##..#.',
        '..#.##.....',
        '.#.#.#....#',
        '.#........#',
        '#.##...#...',
        '#...##....#',
        '.#..#...#.#',
    ]

# Act
    actual = day3.count_trees(path, local_map)

    # Assert
    assert actual == expected




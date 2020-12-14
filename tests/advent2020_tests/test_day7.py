#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day7_handy_haversacks as day7

_MODULE = 'advent_of_code.advent2020.day7_handy_haversacks'


RULE_1 = ['light red bags contain 1 bright white bag, 2 muted yellow bags.']
RULE_2 = ['bright white bags contain 1 shiny gold bag.']
RULE_3 = ['dotted black bags contain no other bags.']
# PARSED_RULE_1 = {'light red': {'bright white': 1, 'muted yellow': 2}}
# PARSED_RULE_2 = {'bright white': {'shiny gold': 1}}
# PARSED_RULE_3 = {'dotted black': {}}
# PARSED_RULE_4 = {'dark orange': {'bright white bags': 3, 'muted yellow bags': 4}}
# PARSED_RULE_5 = {'muted yellow': {'shiny gold bags': 2, 'faded blue bags': 9}}
# PARSED_RULE_6 = {'shiny gold': {'dark olive bag': 1, 'vibrant plum bags': 2}}
# PARSED_RULE_7 = {'dark olive': {'faded blue bags': 3, 'dotted black bags': 4}}
# PARSED_RULE_8 = {'vibrant plum': {'faded blue bags': 5, 'dotted black bags': 6}}
# PARSED_RULE_9 = {'faded blue': {}}
PARSED_RULE_1 = {'light red': [('bright white', 1), ('muted yellow', 2)]}
PARSED_RULE_2 = {'bright white': [('shiny gold', 1)]}
PARSED_RULE_3 = {'dotted black': []}
PARSED_RULE_4 = {'dark orange': [('bright white', 3), ('muted yellow', 4)]}
PARSED_RULE_5 = {'muted yellow': [('shiny gold', 2), ('faded blue', 9)]}
PARSED_RULE_6 = {'shiny gold': [('dark olive', 1), ('vibrant plum', 2)]}
PARSED_RULE_7 = {'dark olive': [('faded blue', 3), ('dotted black', 4)]}
PARSED_RULE_8 = {'vibrant plum': [('faded blue', 5), ('dotted black', 6)]}
PARSED_RULE_9 = {'faded blue': []}
PARSED_RULES = [
    PARSED_RULE_1,
    PARSED_RULE_2,
    PARSED_RULE_3,
    PARSED_RULE_4,
    PARSED_RULE_5,
    PARSED_RULE_6,
    PARSED_RULE_7,
    PARSED_RULE_8,
    PARSED_RULE_9,
]
# [ 'light red bags contain 1 bright white bag, 2 muted yellow bags.',
# 'bright white bags contain 1 shiny gold bag.',
# 'dotted black bags contain no other bags.']
# def test_bags_containing_shiny_gold():
#     # Arrange
#     rules = [
#         'light red bags contain 1 bright white bag, 2 muted yellow bags.',
#         'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#         'bright white bags contain 1 shiny gold bag.',
#         'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#         'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#         'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#         'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#         'faded blue bags contain no other bags.',
#         'dotted black bags contain no other bags.',
#     ]
#     expected = 4
#
#     # Act
#     actual = day7.bags_containing_shiny_gold(rules)
#
#     # Assert
#     assert actual == expected

# @pytest.mark.parametrize([])
# def test_bag():
#     pass


@pytest.mark.parametrize('input_rule, expected', [
    (RULE_1, PARSED_RULE_1),
    (RULE_2, PARSED_RULE_2),
    (RULE_3, PARSED_RULE_3),
])
def test_rule_parser(input_rule, expected):
    """Test day7_handy_haversacks.rule_parser."""

    # Act
    actual = day7.rule_parser(input_rule)

    # Assert
    assert next(actual) == expected


def test_bag_class_init():
    """Test day7_handy_haversacks.Bag()."""

    # Arrange
    bag = day7.Bag('some_bag')

    # Assert
    assert bag.bag == 'some_bag'
    assert bag.outside_bags == []
    assert bag.inside_bags == []


def test_bag_class_add_inside_bags():
    """Test day7_handy_haversacks.Bag.add_inside_bags."""

    # Arrange
    bag = day7.Bag('some_bag')

    # Act
    bag.add_inside_bags([('bag1', 1), ('bag2', 2)])

    # Assert
    assert bag.bag == 'some_bag'
    assert bag.inside_bags == [('bag1', 1), ('bag2', 2)]
    assert bag.outside_bags == []


def test_bag_class_add_outside_bags():
    """Test day7_handy_haversacks.Bag.add_outside_bags."""

    # Arrange
    bag = day7.Bag('some_bag')

    # Act
    bag.add_outside_bags([('bag3', 3), ('bag4', 4)])

    # Assert
    assert bag.bag == 'some_bag'
    assert bag.inside_bags == []
    assert bag.outside_bags == [('bag3', 3), ('bag4', 4)]


# def test_count_containing_bags():
#
#     # Arrange
#     color = 'shiny gold'
#     expected = 4
#
#     # Act
#     actual = day7.count_containing_bags(PARSED_RULES, color)
#
#     # Assert
#     assert actual == expected

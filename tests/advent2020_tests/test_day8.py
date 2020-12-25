#!/usr/bin/env python

import pytest

from advent_of_code.advent2020 import day8_handheld_halting as day8

_MODULE = 'advent_of_code.advent2020.day8_handheld_halting'

PROGRAM = [
    ('nop', 0),
    ('acc', 1),
    ('jmp', 4),
    ('acc', 3),
    ('jmp', -3),
    ('acc', -99),
    ('acc', 1),
    ('jmp', -4),
    ('acc', 6),
]


def test_instruction_parser():
    """Test day8_handheld_halting.instruction_parser.

    return: None
    """

    # Arrange
    lines = [
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6',
    ]
    expected = PROGRAM

    # Act
    actual = day8.instruction_parser(lines)

    # Assert
    assert actual == expected


def test_repaired_instructions():
    """Test day8_handheld_halting.repaired_instructions.

    :return: None
    """

    # Arrange
    program = [
        ('nop', 0),
        ('acc', 1),
        ('jmp', 4),
        ('acc', 3),
        ('jmp', -3),
        ('acc', -99),
        ('acc', 1),
        ('jmp', -4),
        ('acc', 6),
    ]
    rep1 = [
        ('nop', 0),
        ('acc', 1),
        ('nop', 4),
        ('acc', 3),
        ('jmp', -3),
        ('acc', -99),
        ('acc', 1),
        ('jmp', -4),
        ('acc', 6),
    ]
    rep2 = [
        ('nop', 0),
        ('acc', 1),
        ('jmp', 4),
        ('acc', 3),
        ('nop', -3),
        ('acc', -99),
        ('acc', 1),
        ('jmp', -4),
        ('acc', 6),
    ]
    rep3 = [
        ('nop', 0),
        ('acc', 1),
        ('jmp', 4),
        ('acc', 3),
        ('jmp', -3),
        ('acc', -99),
        ('acc', 1),
        ('nop', -4),
        ('acc', 6),
    ]

    # Act
    actual = day8.repaired_instructions(program)

    # Assert
    assert next(actual) == rep1
    assert next(actual) == rep2
    assert next(actual) == rep3


def test_run_program():
    """Test day8_handheld_halting.run_program.

    :return: None
    """

    # Arrange
    program = PROGRAM
    expected = 5

    # Act
    actual = day8.run_program(program)

    # Assert
    assert actual == expected

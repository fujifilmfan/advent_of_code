#!/usr/bin/env python
"""
Part 1
Immediately before any instruction is executed a second time, what
value is in the accumulator?

Part 2
What is the value of the accumulator after the program terminates?
"""

import argparse


def parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Boot code options')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a 
                        plaintext file with each record on its own line.
                        """)
    return parser.parse_args(args)


def lines_from_file(path):
    """Yield lines from a file.

    :param path: STR; path to input file
    :return: OBJ; generator
    """

    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def main(args):
    cli_args = parsed_args(args)
    path = cli_args.filename
    instruction_list = instruction_parser(lines_from_file(path))

    print(f"Part 1 acc: {run_program(instruction_list)}")
    count = 0

    for instruction in repaired_instructions(instruction_list):
        acc = run_repaired_program(instruction)
        count += 1
        # print(f"count: {count}")
        if acc is not None:
            print(f"Part 2 acc: {acc}")
            return acc


def instruction_parser(lines):
    instructions = []

    for line in lines:
        op, num = line.split(' ')
        instructions.append((op, int(num)))

    return instructions


def repaired_instructions(instructions):
    i = 0
    while i < len(instructions):
        op, num = instructions[i]
        if op == 'nop' and num != 0:
            instructions[i] = ('jmp', num)
            yield instructions
            instructions[i] = ('nop', num)
        elif op == 'jmp':
            instructions[i] = ('nop', num)
            yield instructions
            instructions[i] = ('jmp', num)
        i += 1


def run_program(instructions):
    """Instruction list, whether repaired or not.

    :param instructions: LIST
    :return: INT
    """

    executed = set()
    acc = 0
    i = 0

    while i not in executed:
        executed.add(i)
        op, num = instructions[i]

        if op == 'nop':
            i += 1
        elif op == 'acc':
            acc += num
            i += 1
        elif op == 'jmp':
            i += num

    return acc


def run_repaired_program(instructions):
    """Instruction list, whether repaired or not.

    :param instructions: LIST
    :return: INT
    """

    executed = set()
    acc = 0
    i = 0

    while i not in executed:
        executed.add(i)
        try:
            op, num = instructions[i]
        except IndexError:
            return acc
        else:
            if op == 'nop':
                i += 1
            elif op == 'acc':
                acc += num
                i += 1
            elif op == 'jmp':
                i += num

    # return acc


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 1818
# Part Two
# 631

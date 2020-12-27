#!/usr/bin/env python
"""
Part 1
If you use every adapter in your bag at once, what is the distribution
of joltage differences between the charging outlet, the adapters, and
your device?

Part 2
What is the total number of distinct ways you can arrange the adapters
to connect the charging outlet to your device?
"""

import argparse
from itertools import combinations


def parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Adapter array options')
    parser.add_argument('filename', type=str, help="""
                        Required. Enter the path to the input file that 
                        you would like to analyze. The file should be a 
                        plaintext file with each record on its own line.
                        """)
    return parser.parse_args(args)


def lines_from_file(path):
    """Return lines from a file. Add outlet and device ratings, too.

    :param path: STR; path to input file
    :return: OBJ; generator
    """

    # Initialize list with 0 for the outlet.
    file_contents = [0]
    with open(path) as handle:
        for line in handle:
            file_contents.append(int(line.rstrip('\n')))
    # Add the device rating to the list.
    file_contents.append(max(file_contents)+3)
    file_contents.sort()

    return file_contents


def main(args):
    cli_args = parsed_args(args)
    path = cli_args.filename

    adapters = lines_from_file(path)
    distribution = joltage_diff_distribution(adapters)

    solution = 1
    for k, v in distribution.items():
        solution *= v

    anchor_indices = anchor_adapter_indices(adapters)
    gaps = identify_optional_and_required_adapters(anchor_indices)
    arrangements = calculate_arrangements(gaps)

    print(arrangements)
    return arrangements


def joltage_diff_distribution(adapters):
    """Find joltage diffs between consecutive adapters.

    This will return a data structure like {1: 22, 3: 10}.

    :param adapters: LIST; ints of adapter ratings
    :return: DICT; counts of 1 and 3 joltage differences
    """

    distribution = {1: 0, 3: 0}

    for i, adapter in enumerate(adapters):
        try:
            adap1, adap2 = adapters[i], adapters[i+1]
        except IndexError:
            break
        else:
            diff = adap2 - adap1
            distribution[diff] += 1

    return distribution


def anchor_adapter_indices(adapters):
    """Get index of each adapter rating that must remain in the chain.

    :param adapters: LIST; ints of adapter ratings
    :return: LIST; ints representing indices of adapter ratings
        that cannot be removed from the chain
    """

    # Initialize with 0 for the outlet (if the first adapter is not
    # 3, then this wouldn't get added.
    anchor_indices = [0]

    for i, adapter in enumerate(adapters):
        try:
            adap1, adap2 = adapters[i], adapters[i+1]
        except IndexError:
            break
        else:
            if adap2 - adap1 == 3:
                if i not in anchor_indices:
                    anchor_indices.append(i)
                anchor_indices.append(i+1)

    return list(anchor_indices)


def identify_optional_and_required_adapters(anchor_indices):
    """Determine whether numbers in gaps are optional or required.

    This will return a data structure like:
    {
        'optional': [2, 1],
        'required': [3, 3, 3, 3],
    }
    Here, the '2' means that there is a gap which two numbers can
    optionally fill.  The '3's represent gaps in which one of the three
    numbers is required, which would result in 2^3 - 1 arrangements.

    :param anchor_indices: LIST; ints representing indices of adapter ratings
        that cannot be removed from the chain
    :return: DICT; contains lists of gap sizes
    """

    optional_and_required = {
        'optional': [],
        'required': [],
    }

    for i, anchor in enumerate(anchor_indices):
        try:
            index1, index2 = anchor_indices[i], anchor_indices[i+1]
        except IndexError:
            break
        else:
            gap_size = index2 - index1 - 1
            if gap_size == 0:
                continue
            elif gap_size < 3:
                optional_and_required['optional'].append(gap_size)
            else:
                optional_and_required['required'].append(gap_size)

    return optional_and_required


def calculate_arrangements(gaps):
    """Calculate the number of arrangements from gap sizes.

    :param gaps: DICT; contains lists of gap sizes; see note in
        identify_optional_and_required_adapters()
    :return: INT; total number of arrangements
    """

    arrangements = 1

    optional = gaps['optional']
    required = gaps['required']

    for num in optional:
        arrangements *= 2**num
    for num in required:
        arrangements *= 2**num - 1

    return arrangements


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 1755 - {1: 65, 3: 27}
# Part Two
# 4049565169664 (4,049,565,169,664)

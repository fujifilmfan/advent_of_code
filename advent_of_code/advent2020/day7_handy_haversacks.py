#!/usr/bin/env python
"""
Part 1
How many bag colors can eventually contain at least one shiny gold bag?

Part 2

"""

import argparse
import re


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(
        description='Valid password count')
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
    cli_args = return_parsed_args(args)
    path = cli_args.filename
    rules = rules_from_file(path)
    bag_map = create_bag_map(rules)
    outside_bags = containing_bags(bag_map, 'shiny gold')
    print(len(outside_bags))
    inside_bags = contained_bags(bag_map, 'shiny gold', 1)
    print(inside_bags)


def rules_from_file(path):
    """Read lines from file and yield group responses from input file.

    :param path: STR; path to input file
    :return: OBJ; generator
    """

    rules = lines_from_file(path)
    yield from rule_parser(rules)


def rule_parser(lines):
    """Parse rules and create a dictionary of the rule.

    The first regex will produce data like:
        'dotted black' 'no other bags' or
        'light red' '1 bright white bag, 2 muted yellow bags.'
    The `if` function will produce data like:
        'dotted black': {}
    The second regex and dict comprehension will produce data like:
        'light red': {'bright white': 1, 'muted yellow': 2}

    :param lines: OBJ; generator object yielding line from file
    :return: OBJ; generator object yielding dict of rule
    """

    # rule = {}
    for line in lines:
        rule = {}
        bag, contents = re.split(' bags contain ', line)
        if 'no other' in contents:
            rule[bag] = None
        matches = re.findall(r'(\d+) (\w+ \w+) bag', contents)
        rule[bag] = [(color, int(count)) for count, color in matches]
        yield rule


def create_bag_map(rules):
    # Create a dict like
    #   {'light red': <__main__.Bag object at 0x1063a2cd0>}
    bags = {}
    for rule in rules:
        for bag, inside_bags in rule.items():
            if bag not in bags:
                bags[bag] = Bag(bag)
            bags[bag].add_inside_bags(inside_bags)

            for inside_bag, count in inside_bags:
                if inside_bag not in bags:
                    bags[inside_bag] = Bag(inside_bag)
                bags[inside_bag].add_outside_bags([bag])
    return bags


def containing_bags(bag_map, bag_color):
    outside_bags = set()
    for bag, obj in bag_map.items():
        for color, count in obj.inside_bags:
            if bag_color == color:
                outside_bags.add(bag)
                outside_bags.update(containing_bags(bag_map, bag))

    return outside_bags


def contained_bags(bag_map, bag_color, num_bags):
    total = 0
    if not bag_map[bag_color].inside_bags:
        return num_bags
    for bag in bag_map[bag_color].inside_bags:
        color, count = bag
        total += contained_bags(bag_map, color, count)
    return total * num_bags + num_bags
    # contained_bags(bag_map, bag_color, )


    # total = 0
    # for color, count in bag_map[bag_color].inside_bags:
    #     total += count
    #     sub_total = contained_bags(bag_map, color)
    #     total *= sub_total if sub_total > 0 else 1
    # return total
# 2+(2*(2+(2*(2+(2*(2+(2*(2+(2*2))))


class Bag:

    def __init__(self, bag):
        self.bag = bag
        self.outside_bags = []
        self.inside_bags = []

    def add_bags(func):
        def wrapper(*args):
            attr, bags = func(*args)
            for bag in bags:
                if bag not in attr:
                    attr.append(bag)
        return wrapper

    @add_bags
    def add_inside_bags(self, bags):
        return self.inside_bags, bags

    @add_bags
    def add_outside_bags(self, bags):
        return self.outside_bags, bags


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

# Part One
# 222
# Part Two
# 13264 (code gives 13265)

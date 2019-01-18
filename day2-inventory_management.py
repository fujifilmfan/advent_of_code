#!/usr/bin/env python

import argparse
from collections import Counter
from string import ascii_lowercase as letters

from file_ops import return_file_contents


class Checksum(object):

    def __init__(self):
        parser = self.create_parser()
        self.args = parser.parse_args()
        self.box_ids = return_file_contents(self.args.read_file_name)
        self.twos = set()
        self.threes = set()

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser(
            description='Box ID processing options.')

        parser.add_argument('read_file_name', type=str, help="""
                            Required. Enter the path to the input file that you
                            would like to analyze.  The file should be a
                            plaintext file with each record on its own line.
                            """)

        return parser

    def find_repeats(self):
        for box_id in self.box_ids:
            counter = Counter(box_id)
            for letter in box_id:
                if counter[letter] == 2:
                    self.twos.add(box_id)
                if counter[letter] == 3:
                    self.threes.add(box_id)

    def calculate_checksum(self):
        checksum = len(self.twos) * len(self.threes)
        return checksum

    def find_box_ids_that_differ_by_one_char(self):
        for i, _ in enumerate(self.box_ids):
            for j, _ in enumerate(self.box_ids):
                common = ""
                different = ""
                strings_to_compare = zip(self.box_ids[i], self.box_ids[j])
                for k, l in strings_to_compare:
                    if k == l:
                        common += k
                    else:
                        different += k
                if len(different) == 1:
                    return common


def generate_checksum():
    checksum = Checksum()
    checksum.find_repeats()
    print("checksum: {checksum}".format(checksum=checksum.calculate_checksum()))
    print("common letters: {letters}".format(letters=checksum.find_box_ids_that_differ_by_one_char()))


if __name__ == '__main__':
    generate_checksum()

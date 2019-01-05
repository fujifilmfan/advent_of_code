#!/usr/bin/env python

import argparse
from collections import Counter

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


class Checksum(object):

    def __init__(self):
        parser = self.create_parser()
        self.args = parser.parse_args()
        self.box_ids = self.load_box_ids_from_file(self.args.read_file_name)
        self.twos = set()
        self.threes = set()

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser(
            description='Frequency processing options.')

        parser.add_argument('read_file_name', type=str, help="""
                            Required. Enter the path to the frequency changes
                            file that you would like analyze.  The file should
                            be a plaintext file with each frequency change on
                            its own line.
                            """)

        return parser

    @staticmethod
    def load_box_ids_from_file(filename):
        """Open file specified from user input and read in the frequency changes."""
        box_ids = []
        with open(filename) as inventory_file:
            for box_id in inventory_file:
                box_ids.append(box_id)
        return box_ids

    def find_repeats(self):
        for box_id in self.box_ids:
            counter = Counter(box_id)
            for letter in ALPHABET:
                if counter[letter] == 2:
                    self.twos.add(box_id)
                if counter[letter] == 3:
                    self.threes.add(box_id)

    def calculate_checksum(self):
        checksum = len(self.twos) * len(self.threes)
        return checksum

    def find_box_ids_that_differ_by_one_char(self):
        i = 0
        while i < len(self.box_ids) - 1:
            j = 1
            while j < len(self.box_ids):
                common = ""
                different = ""
                strings_to_compare = zip(self.box_ids[i], self.box_ids[j])
                for k,l in strings_to_compare:
                    if k == l:
                        common += k
                    else:
                        different += k
                if len(different) == 1:
                    return common
                j += 1
            i += 1



def generate_checksum():
    checksum = Checksum()
    checksum.find_repeats()
    print("checksum: {checksum}".format(checksum=checksum.calculate_checksum()))
    print("common letters: {letters}".format(letters=checksum.find_box_ids_that_differ_by_one_char()))


if __name__ == '__main__':
    generate_checksum()

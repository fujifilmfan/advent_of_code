#!/usr/bin/env python

import argparse


class Frequency(object):

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
    def load_frequency_changes_from_file(filename):
        """Open file specified from user input and read in the frequency changes."""
        freq_changes = []
        with open(filename) as frequency_file:
            for change in frequency_file:
                freq_changes.append(change)
        return freq_changes

    def sum_frequencies(self, args):
        changes = self.load_frequency_changes_from_file(args.read_file_name)
        freq = 0
        for change in changes:
            freq += int(change)
        return freq


def calculate_frequency():
    frequency = Frequency()
    parser = frequency.create_parser()
    args = parser.parse_args()
    calculated_frequency = frequency.sum_frequencies(args)
    print(calculated_frequency)


if __name__ == '__main__':
    calculate_frequency()

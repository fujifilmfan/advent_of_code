#!/usr/bin/env python

import argparse
from itertools import cycle

from . import file_ops


class Frequency(object):

    def __init__(self):
        parser = self.create_parser()
        self.args = parser.parse_args()
        self.changes = file_ops.return_file_contents(
            self.args.read_file_name, 'int')

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser(
            description='Frequency processing options.')

        parser.add_argument('read_file_name', type=str, help="""
                            Required. Enter the path to the input file that you
                            would like to analyze.  The file should be a
                            plaintext file with each record on its own line.
                            """)
        parser.add_argument('-d', '--find_first_duplicate', action='store_true',
                            help="""Find first duplicate frequency.""")
        parser.add_argument('-s', '--sum_frequencies', action='store_true',
                            help="""Sum the frequency changes in the input
                            file""")

        return parser

    def process_request(self):
        results = {}
        message = "Use the -s or -d flag to see the frequency sum or first duplicate, respectively."
        if not self.args.sum_frequencies and not self.args.find_first_duplicate:
            return message
        else:
            if self.args.sum_frequencies:
                frequency_sum = self.sum_frequencies()
                results['frequency_sum'] = frequency_sum
            else:
                pass
            if self.args.find_first_duplicate:
                first_duplicate = self.find_first_duplicate()
                results['first_duplicate'] = first_duplicate
            else:
                pass
            return results

    def sum_frequencies(self):
        freq = 0
        for change in self.changes:
            freq += change
        return freq

    def find_first_duplicate(self):
        freq = 0
        seen = set()
        i = 0
        for change in cycle(self.changes):
            if i == 200000:
                break
            else:
                freq += change
                if freq in seen:
                    return freq
                else:
                    seen.add(freq)
                    i += 1


def analyze_frequency():
    frequency = Frequency()
    frequency_analysis = frequency.process_request()
    print(frequency_analysis)


if __name__ == '__main__':
    analyze_frequency()

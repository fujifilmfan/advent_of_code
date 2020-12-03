#!/usr/bin/env python

import argparse
from itertools import product

from . import file_ops


class Claims(object):

    def __init__(self):
        parser = self.create_parser()
        self.args = parser.parse_args()
        self.claims = file_ops.return_file_contents(self.args.read_file_name)
        self.coord_tuples = {}
        self.claimed_once = set()
        self.claimed_more_than_once = set()
        self.nonoverlapping_claims = []

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser(
            description='Fabric claim processing options.')

        parser.add_argument('read_file_name', type=str, help="""
                            Required. Enter the path to the input file that you
                            would like to analyze.  The file should be a
                            plaintext file with each record on its own line.
                            """)

        return parser

    def process_claims(self):
        """Call methods to parse claims and determine coordinate pairs."""
        claim_dict = self.split_claims()
        coords = self.enumerate_coordinates(claim_dict)
        # self.create_coord_tuples() returns a class variable
        self.create_coord_tuples(coords)

    def split_claims(self):
        """Returns a dictionary with claim IDs as keys and dictionaries of claim dimensions as values:
        {'742': {'left': 569, 'top': 431, 'width': 23, 'height': 17},
        '1237': {'left': 275, 'top': 930, 'width': 15, 'height': 18}}
        """
        claim_dict = {}
        for claim in self.claims:
            claim_list = claim.replace('#', '').replace('@ ', '').replace(',', ' ').replace(':', '').\
                               replace('x', ' ').split()
            claim_dict[claim_list[0]] = {'left': int(claim_list[1]), 'top': int(claim_list[2]),
                                         'width': int(claim_list[3]), 'height': int(claim_list[4])}
        return claim_dict

    @staticmethod
    def enumerate_coordinates(claim_dict):
        """Returns a dictionary with claim IDs as keys and dictionaries of columns and rows as values:
        {'742': {'columns': [569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586,
        587, 588, 589, 590, 591], 'rows': [431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445,
        446, 447], ...}
        """
        coords = {}
        for key in claim_dict:
            coords[key] = {'columns': [], 'rows': []}
            for column in range(claim_dict[key]['left'], claim_dict[key]['left'] + claim_dict[key]['width']):
                coords[key]['columns'].append(column)
            for row in range(claim_dict[key]['top'], claim_dict[key]['top'] + claim_dict[key]['height']):
                coords[key]['rows'].append(row)
        return coords

    def create_coord_tuples(self, coords):
        """Returns a dictionary with claim IDs as keys and a list of coordinate pairs as values:
        {'742': [(569, 431), (569, 432), (569, 433), (569, 434), (569, 435), (569, 436), (569, 437), (569, 438),
        (569, 439), (569, 440), ...]}
        """
        for key in coords:
            columns = coords[key]['columns']
            rows = coords[key]['rows']
            self.coord_tuples[key] = list(product(columns, rows))
        return self.coord_tuples

    def find_coord_overlaps(self):
        """Adds coordinates to self.claimed_once when seen for the first time and to self.claimed_more_than_once if
        already found in self.claimed_once.  Finally, the length of each set is returned."""
        for key in self.coord_tuples:
            for coord in self.coord_tuples[key]:
                if coord in self.claimed_once:
                    self.claimed_more_than_once.add(coord)
                else:
                    self.claimed_once.add(coord)
        return "Number of square inches claimed once: {once}\n" \
               "Number of square inches claimed more than once: {more}".format(once=len(self.claimed_once),
                                                                               more=len(self.claimed_more_than_once))

    def find_nonoverlapping_claims(self):
        """Finds claims that do not overlap with any others by comparing the coordinates of each claim to the set
        self.claimed_more_than_once.  Both process_claims() and find_coord_overlaps() need to run first."""
        for key in self.coord_tuples:
            non_overlapping = not any(coord in self.claimed_more_than_once for coord in self.coord_tuples[key])
            if non_overlapping is True:
                self.nonoverlapping_claims.append(key)
        return "Non-overlapping claim IDs: {claims}".format(claims=self.nonoverlapping_claims)


def analyze_claims():
    claims = Claims()
    claims.process_claims()
    print(claims.find_coord_overlaps())
    print(claims.find_nonoverlapping_claims())


if __name__ == '__main__':
    analyze_claims()

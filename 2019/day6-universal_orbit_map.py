#!/usr/bin/env python

import argparse

from file_ops import return_file_contents


"""
A note on terminology used in this script: in the simple sequence 
COM - B - C, call B a 'body'.  Then COM is B's 'primary', and C is B's 
'satellite'.
"""

# Create a dictionary in which each body is a key containing a Body
# object value.
body_objects = {}


def create_body_objects(map_):
    for location in map_:
        objects = location.split(')')
        body = objects[0]
        satellite = objects[1]

        # Add the body to the object dictionary.
        if body not in body_objects:
            body_objects[body] = Body(body)
        body_objects[body].add_satellite(satellite)

        # The satellite needs to have a key in the object dict, too.
        if satellite not in body_objects:
            body_objects[satellite] = Body(satellite)
        # Add the body around which the satellite orbits to its
        # object representation.
        body_objects[satellite].add_primary(body)


def count_connections(body):

    connections = 0

    # Call calc_distance_to_x on each body and add the resulting values
    # to connections.
    for k, v in body_objects.items():
        v.calc_distance_to_x(body, body_objects)

        connections += v.distance_to_x

    return connections


class Body:

    def __init__(self, me):
        self.me = me
        # The object around which this body orbits. There can be only 1.
        self.primary = None
        # The objects that orbit this body.
        self.satellites = []

        self.distance_to_x = 0

    def add_primary(self, primary):
        self.primary = primary

    def add_satellite(self, satellite):
        if satellite not in self.satellites:
            self.satellites.append(satellite)

    def calc_distance_to_x(self, x, map_):
        """Determine distance to an arbitrary node x.

        This only works in one direction, from body to primary, not
        from body to satellite.

        :param x: STR
        :param map_: DICT
        :return: INT
        """

        connections = 0
        x_found = False

        ancestor = self.primary
        while x_found is False:
            if ancestor is None:
                break
            elif ancestor == x:
                connections += 1
                x_found = True
            elif body_objects[ancestor].distance_to_x != 0:
                connections += 1 + body_objects[ancestor].distance_to_x
                x_found = True
            else:
                connections += 1
                ancestor = body_objects[ancestor].primary

        self.distance_to_x = connections


        # while ancestor is not x:
        #     # If ancestor is None, then I'm COM, and distance to x
        #     # remains 0 regardless of who x is.
        #     if ancestor is None:
        #         break
        #     elif body_objects[ancestor].distance_to_x == 0:
        #         # Add the distance to the primary to connections, then
        #         # set the ancestor to be that primary's primary.
        #         connections += 1
        #         ancestor = body_objects[ancestor].primary
        #     else:
        #         # Add the distance to the primary to the primary's
        #         # distance to x.
        #         connections = 1 + body_objects[ancestor].distance_to_x
        #         break

        # self.distance_to_x = connections


def print_body_objects():
    """
    Sample output:

    COM - primary: None; satellites: ['B']
    B - primary: COM; satellites: ['C', 'G']
    C - primary: B; satellites: ['D']
    D - primary: C; satellites: ['E', 'I']
    E - primary: D; satellites: ['F', 'J']
    F - primary: E; satellites: []
    G - primary: B; satellites: ['H']
    H - primary: G; satellites: []
    I - primary: D; satellites: []
    J - primary: E; satellites: ['K']
    K - primary: J; satellites: ['L']
    L - primary: K; satellites: []

    :return: None
    """

    for k, v in body_objects.items():
        # if len(v.satellites) > 1:
        print(f"{k} - "
              f"me: {v.me}; "
              f"primary: {v.primary}; "
              f"satellites: {v.satellites}; "
              f"distance_to_x: {v.distance_to_x}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Intcode computer solution options.')

    parser.add_argument('read_file_name', type=str, help="""
                        Required. Enter the path to the input file that you
                        would like to analyze.  The file should be a
                        plaintext file with each record on its own line.
                        """)
    args = parser.parse_args()
    program_input = return_file_contents(args.read_file_name)
    create_body_objects(program_input)
    print(count_connections('62D'))
    # print_body_objects()


# Part One: 314247
# Part Two:

"""
First strategy:
Starting with 'COM', search the input for all entries beginning with
each primary body.  When one is found, add the satellite to orbit_count
as a key and set the value to (1 + the count for the primary).  In the
end, add all of the counts.  This is slow (~n^2) due to searching the 
list as many times as the number of entries.  After searching the list 
for  all instances of a planet, move the found satellites to the 
primaries list for the next iteration.
Example map:
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
For the example, orbit_count looks like this after the last iteration:
{
    'COM': 0,
    'B': 1,
    'C': 2,
    'G': 2,
    'D': 3,
    'H': 3,
    'E': 4,
    'I': 4,
    'F': 5,
    'J': 5,
    'K': 6,
    'L': 7
}
"""
# def count_total_orbits(map):
#
#     orbit_count = {
#         'COM': 0
#     }
#     distance = 0
#     iterations = 0
#     primaries = ['COM']
#     satellites = []
#
#     while iterations < len(map):
#         for location in map:
#             bodies = location.split(')')
#             for primary in primaries:
#                 if bodies[0] == primary:
#                     satellites.append(bodies[1])
#                     orbit_count[bodies[1]] = (1 + orbit_count[primary])
#                     iterations += 1
#         primaries = satellites
#         satellites = []
#
#     print(orbit_count)
#
#     count = 0
#     for k,v in orbit_count.items():
#         count += v
#     print(count)

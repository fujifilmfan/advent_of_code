#!/usr/bin/env python

import argparse

from file_ops import return_file_contents


def record_nodes(wire_path):

    nodes = [(0, 0)]
    x = 0
    y = 0

    for wire_segment in wire_path:

        dir_ = wire_segment[0]
        mag = int(wire_segment[1:])

        if dir_ == 'R':
            x += mag
            nodes.append((x, y))

        elif dir_ == 'L':
            x -= mag
            nodes.append((x, y))

        elif dir_ == 'U':
            y += mag
            nodes.append((x, y))

        elif dir_ == 'D':
            y -= mag
            nodes.append((x, y))

        else:
            print(f"Which direction should I go? You told me {dir_}")

    return nodes


def find_crossings(nodes, wire_path):

    wire_1_nodes = nodes
    previous_node = (0, 0)
    x = 0
    y = 0
    all_crossings = []

    for wire_segment in wire_path:

        dir_ = wire_segment[0]
        mag = int(wire_segment[1:])

        if dir_ == 'R':
            x += mag

        elif dir_ == 'L':
            x -= mag

        elif dir_ == 'U':
            y += mag

        elif dir_ == 'D':
            y -= mag

        else:
            print(f"Which direction should I go? You told me {dir_}")

        current_node = (x, y)
        crossings = check_for_crossing(
            wire_1_nodes, previous_node, current_node)
        if len(crossings) > 0:
            all_crossings.extend(crossings)
        previous_node = current_node
    
    return all_crossings


def check_for_crossing(nodes, previous_node, current_node):
    
    crossings = []
    i = 0
    while i <= len(nodes):
        for i in range(len(nodes) - 1):
    
            first = nodes[i]
            second = nodes[i+1]
    
            if (previous_node[0] == current_node[0] and (
                    (first[0] <= previous_node[0] and previous_node[0] <= (second)[0]) or
                    (first[0] >= previous_node[0] and previous_node[0] >= (second)[0])
                ) and (
                    (first[1] <= previous_node[1] and 
                     current_node[1] <= first[1] and
                     (second)[1] <= previous_node[1] and
                     current_node[1] <= (second)[1]
                    ) or
                    (first[1] >= previous_node[1] and
                     current_node[1] >= first[1] and
                     (second)[1] >= previous_node[1] and
                     current_node[1] >= (second)[1]
                    )
                )
            ):
                crossings.append((previous_node[0], first[1]))
                i += 1
            
            elif (previous_node[1] == current_node[1] and (
                    (first[1] <= previous_node[1] and previous_node[1] <= (second)[1]) or
                    (first[1] >= previous_node[1] and previous_node[1] >= (second)[1])
                ) and (
                    (first[0] <= previous_node[0] and 
                     current_node[0] <= first[0] and
                     (second)[0] <= previous_node[0] and
                     current_node[0] <= (second)[0]
                    ) or
                    (first[0] >= previous_node[0] and
                     current_node[0] >= first[0] and
                     (second)[0] >= previous_node[0] and
                     current_node[0] >= (second)[0]
                    )
                )
            ):
                crossings.append((first[0], previous_node[1]))
                i += 1
                
            else:
                i += 1 

        break

    return crossings


def find_shortest_distance(crossings):

    shortest_d = 1000000

    intersections = crossings[1:]

    for intersection in intersections:
        x = abs(intersection[0])
        y = abs(intersection[1])
        if (abs(x) + abs(y)) < shortest_d:
            shortest_d = (abs(x) + abs(y))

    return shortest_d


def find_shortest_path():
    pass


def solve_crossed_wires(wire_paths):
    
    wire_path_1 = wire_paths[0].split(',')
    wire_path_2 = wire_paths[1].split(',')
    
    nodes = record_nodes(wire_path_1)
    crossings = find_crossings(nodes, wire_path_2)
    print(crossings)

    shortest_distance = find_shortest_distance(crossings)  
    print(shortest_distance)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Crossed wires solution options.')

    parser.add_argument('read_file_name', type=str, help="""
                        Required. Enter the path to the input file that you
                        would like to analyze.  The file should be a
                        plaintext file with each record on its own line.
                        """)
    args = parser.parse_args()
    wire_paths = return_file_contents(args.read_file_name)
    solve_crossed_wires(wire_paths)

# Part One:
# 1211
# Part Two:

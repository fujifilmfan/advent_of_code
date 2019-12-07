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
    
            # TODO: Clean up this mess
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


def find_manhattan_distance(crossings):

    shortest_d = 1000000

    intersections = crossings[1:]

    for intersection in intersections:
        x = abs(intersection[0])
        y = abs(intersection[1])
        if (abs(x) + abs(y)) < shortest_d:
            shortest_d = (abs(x) + abs(y))

    return shortest_d


def traverse_path_to_crossings(crossings, wire_path):
    
    x = 0
    y = 0
    distance_traversed = 0
    crossing_distances = []

    for wire_segment in wire_path:

        dir_ = wire_segment[0]
        mag = int(wire_segment[1:])
        
        if dir_ == 'R':
            for i in range(mag):
                distance_traversed += 1
                x += 1
                if is_current_point_a_crossing(crossings, (x, y)):
                    crossing_distances.append((x, y))
                    crossing_distances.append(distance_traversed)

        elif dir_ == 'L':
            for i in range(mag):
                distance_traversed += 1
                x -= 1
                if is_current_point_a_crossing(crossings, (x, y)):
                    crossing_distances.append((x, y))
                    crossing_distances.append(distance_traversed)

        elif dir_ == 'U':
            for i in range(mag):
                distance_traversed += 1
                y += 1
                if is_current_point_a_crossing(crossings, (x, y)):
                    crossing_distances.append((x, y))
                    crossing_distances.append(distance_traversed)

        elif dir_ == 'D':
            for i in range(mag):
                distance_traversed += 1
                y -= 1
                if is_current_point_a_crossing(crossings, (x, y)):
                    crossing_distances.append((x, y))
                    crossing_distances.append(distance_traversed)

        else:
            print(f"Which direction should I go? You told me {dir_}")

    return crossing_distances


def is_current_point_a_crossing(crossings, current_point):

    for crossing in crossings:
        if crossing == current_point:
            return True
    return False


def find_shortest_combined_path(crossings, crossing_distances):
    
    shortest_distance = 1000000
    
    for crossing in crossings:
        distance = 0
        for crossing_distance in crossing_distances:
            for i in range(len(crossing_distance)):
                if crossing_distance[i] == crossing:
                    distance += crossing_distance[i + 1]
        if distance < shortest_distance:
            shortest_distance = distance
    
    return shortest_distance
                    

def solve_crossed_wires(wire_paths):
    
    wire_path_1 = wire_paths[0].split(',')
    wire_path_2 = wire_paths[1].split(',')
    
    nodes = record_nodes(wire_path_1)
    crossings = find_crossings(nodes, wire_path_2)
    print(crossings)

    shortest_distance = find_manhattan_distance(crossings)  
    print(shortest_distance)
    
    crossing_distances_1 = traverse_path_to_crossings(crossings, wire_path_1)
    crossing_distances_2 = traverse_path_to_crossings(crossings, wire_path_2)
    print(crossing_distances_1, crossing_distances_2)

    crossing_distances = [crossing_distances_1, crossing_distances_2]
    shortest_combined_path = find_shortest_combined_path(
        crossings[1:], crossing_distances)
    print(shortest_combined_path)


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
# 101386

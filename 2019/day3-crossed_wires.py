#!/usr/bin/env python

import argparse
import numpy as np
from copy import deepcopy

from file_ops import return_file_contents


def determine_array_size(wire_paths):
    
    max_pos_x = 0
    max_neg_x = 0
    max_pos_y = 0
    max_neg_y = 0
    
    for wire_path in wire_paths:
        cur_x = 0
        cur_y = 0
        
        # Create list from input row.
        wire_path_list = [i for i in wire_path.split(',')]

        for wire_segment in wire_path_list:
            dir = wire_segment[0]
            mag = int(wire_segment[1:])
            
            if dir == 'R':
                max_pos_x = cur_x + mag if cur_x + mag > max_pos_x else max_pos_x
                cur_x += mag
            
            elif dir == 'L':
                max_neg_x = cur_x - mag if cur_x - mag < max_neg_x else max_neg_x
                cur_x -= mag
                
            elif dir == 'U':
                max_pos_y = cur_y + mag if cur_y + mag > max_pos_y else max_pos_y
                cur_y += mag

            elif dir == 'D':
                max_neg_y = cur_y - mag if cur_y - mag < max_neg_y else max_neg_y
                cur_y -= mag
            
            else:
                print(f"Which direction should I go? You told me {dir}")
            
    total_x = abs(max_pos_x) + abs(max_neg_x)
    total_y = abs(max_pos_y) + abs(max_neg_y)
    
    # Set central port coordinates to lower left corner of array.
    central_port_x = 0 - max_neg_x
    central_port_y = total_y + max_neg_y

    # Add 1 so that the totals are inclusive.
    array_stats = {
        'total_x': 1+ total_x,
        'total_y': 1+ total_y,
        'central_port_x': central_port_x,
        'central_port_y': central_port_y,
    }

    return array_stats


def create_numpy_array(array_stats):
    
    # Create NumPy array initialized with zeros.
    array = np.zeros((array_stats['total_y'], array_stats['total_x']))

    return array


def plot_path(wire_path, array_stats, array, threshold):
    
    array_w_paths = array
    
    cur_x = array_stats['central_port_x']
    cur_y = array_stats['central_port_y']

    # Create list from input row.
    wire_path_list = [i for i in wire_path.split(',')]

    for wire_segment in wire_path_list:
        dir = wire_segment[0]
        mag = int(wire_segment[1:])

        if dir == 'R':
            for i in range(mag):
                if array_w_paths[cur_y, cur_x + (i + 1)] == threshold:
                    array_w_paths[cur_y, cur_x + (i + 1)] += 1
            cur_x += mag

        elif dir == 'L':
            for i in range(mag):
                if array_w_paths[cur_y, cur_x - (i + 1)] == threshold:
                    array_w_paths[cur_y, cur_x - (i + 1)] += 1
            cur_x -= mag

        elif dir == 'U':
            for i in range(mag):
                if array_w_paths[cur_y - (i + 1), cur_x] == threshold:
                    array_w_paths[cur_y - (i + 1), cur_x] += 1
            cur_y -= mag

        elif dir == 'D':
            for i in range(mag):
                if array_w_paths[cur_y + (i + 1), cur_x] == threshold:
                    array_w_paths[cur_y + (i + 1), cur_x] += 1
            cur_y += mag
        
    return array_w_paths


def calculate_distances(array_stats, array_w_paths):
    
    shortest_d = array_stats['total_x'] + array_stats['total_y']
    
    # Create tuple of arrays.
    results = np.where(array_w_paths == 2)
    
    # Join rows and colums.
    coordinates = list(zip(results[0], results[1]))
    
    for coord in coordinates:
        x_diff = abs(coord[1] - array_stats['central_port_x'])
        y_diff = abs(coord[0] - array_stats['central_port_y'])
        distance = x_diff + y_diff
        shortest_d = distance if distance < shortest_d else shortest_d

    return shortest_d


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
    array_stats = determine_array_size(wire_paths)
    array = create_numpy_array(array_stats)
    array_w_path1 = plot_path(wire_paths[0], array_stats, array, 0)
    array_w_path2 = plot_path(wire_paths[1], array_stats, array_w_path1, 1)
    array_w_path2[array_stats['central_port_y'], array_stats['central_port_x']] = 5
    shortest_distance = calculate_distances(array_stats, array_w_path2)
    print(shortest_distance)

# Part One:
# 1211
# Part Two:

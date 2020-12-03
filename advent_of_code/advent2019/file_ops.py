#!/usr/bin/env python


def return_file_contents(filename, *args):
    """Open specified file and return lines as items in a list"""
    file_contents = []
    with open(filename) as input_file:
        if 'int' in args:
            for line in input_file:
                file_contents.append(int(line))
        else:
            for line in input_file:
                file_contents.append(line.rstrip('\n'))
    return file_contents

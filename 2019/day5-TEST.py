#!/usr/bin/env python

import argparse
from copy import deepcopy

from file_ops import return_file_contents


class RunIntcode:
    """
    Opcodes:
    1: Add parameters 1 and 2 and write output to parameter 3
    2: Multiply parameters 1 and 2 and write output to parameter 3
    3: Save input to parameter
    4: Read output from parameter
    5: 'jump-if-true'; if the first parameter is non-zero, it sets the
        instruction pointer to the value from the second parameter
    6: 'jump-if-false'; if the first parameter is zero, it sets the
        instruction pointer to the value from the second parameter
    7: 'less than'; if the first parameter is less than the second
        parameter, it stores 1 in the position given by the third
        parameter. Otherwise, it stores 0.
    8: 'equals'; if the first parameter is equal to the second
        parameter, it stores 1 in the position given by the third
        parameter. Otherwise, it stores 0.

    99: Halt

    """

    def __init__(self, program, input):
        # self.str_codes = program[0].split(',')
        self.codes = [int(i) for i in program[0].split(',')]
        self.input = input
        self.temp_codes = []

    def get_codes(self):

        return self.codes

    def run_program(self):

        pointer = 0
        outputs = []

        codes = self.get_codes()

        while pointer < len(codes):

            opcode = str(codes[pointer])[-2:]

            if (opcode == '1') or (opcode == '01'):

                input1_mode = 0
                input2_mode = 0
                input1 = 0
                input2 = 0

                if str(codes[pointer])[-3:-2] == '1':
                    input1_mode = 1
                if str(codes[pointer])[-4:-3] == '1':
                    input2_mode = 1

                if input1_mode == 0:
                    input1 = codes[codes[pointer+1]]
                elif input1_mode == 1:
                    input1 = codes[pointer+1]

                if input2_mode == 0:
                    input2 = codes[codes[pointer+2]]
                elif input2_mode == 1:
                    input2 = codes[pointer+2]

                codes[codes[pointer+3]] = input1 + input2

                pointer += 4

            elif (opcode == '2') or (opcode == '02'):

                input1_mode = 0
                input2_mode = 0
                input1 = 0
                input2 = 0

                if str(codes[pointer])[-3:-2] == '1':
                    input1_mode = 1
                if str(codes[pointer])[-4:-3] == '1':
                    input2_mode = 1

                if input1_mode == 0:
                    input1 = codes[codes[pointer+1]]
                elif input1_mode == 1:
                    input1 = codes[pointer+1]

                if input2_mode == 0:
                    input2 = codes[codes[pointer+2]]
                elif input2_mode == 1:
                    input2 = codes[pointer+2]

                codes[codes[pointer+3]] = input1 * input2

                pointer += 4

            elif (opcode == '3') or (opcode == '03'):

                input = self.input
                codes[codes[pointer+1]] = input

                pointer += 2

            elif (opcode == '4') or (opcode == '04'):

                input_mode = 0
                output = None

                if str(codes[pointer])[-3:-2] == '1':
                    input_mode = 1

                if input_mode == 0:
                    output = codes[codes[pointer+1]]
                elif input_mode == 1:
                    output = codes[pointer+1]

                outputs.append(output)

                pointer += 2

            elif (opcode == '5') or (opcode == '05'):

                input1_mode = 0
                input2_mode = 0
                input1 = 0
                input2 = 0

                if str(codes[pointer])[-3:-2] == '1':
                    input1_mode = 1
                if str(codes[pointer])[-4:-3] == '1':
                    input2_mode = 1

                if input1_mode == 0:
                    input1 = codes[codes[pointer+1]]
                elif input1_mode == 1:
                    input1 = codes[pointer+1]

                if input2_mode == 0:
                    input2 = codes[codes[pointer+2]]
                elif input2_mode == 1:
                    input2 = codes[pointer+2]

                if input1 != 0:
                    pointer = input2
                else:
                    pointer += 3

            elif (opcode == '6') or (opcode == '06'):

                input1_mode = 0
                input2_mode = 0
                input1 = 0
                input2 = 0

                if str(codes[pointer])[-3:-2] == '1':
                    input1_mode = 1
                if str(codes[pointer])[-4:-3] == '1':
                    input2_mode = 1

                if input1_mode == 0:
                    input1 = codes[codes[pointer+1]]
                elif input1_mode == 1:
                    input1 = codes[pointer+1]

                if input2_mode == 0:
                    input2 = codes[codes[pointer+2]]
                elif input2_mode == 1:
                    input2 = codes[pointer+2]

                if input1 == 0:
                    pointer = input2
                else:
                    pointer += 3

            elif (opcode == '7') or (opcode == '07'):

                input1_mode = 0
                input2_mode = 0
                input1 = 0
                input2 = 0

                if str(codes[pointer])[-3:-2] == '1':
                    input1_mode = 1
                if str(codes[pointer])[-4:-3] == '1':
                    input2_mode = 1

                if input1_mode == 0:
                    input1 = codes[codes[pointer+1]]
                elif input1_mode == 1:
                    input1 = codes[pointer+1]

                if input2_mode == 0:
                    input2 = codes[codes[pointer+2]]
                elif input2_mode == 1:
                    input2 = codes[pointer+2]

                if input1 < input2:
                    codes[codes[pointer+3]] = 1
                else:
                    codes[codes[pointer+3]] = 0

                pointer += 4

            elif (opcode == '8') or (opcode == '08'):

                input1_mode = 0
                input2_mode = 0
                input1 = 0
                input2 = 0

                if str(codes[pointer])[-3:-2] == '1':
                    input1_mode = 1
                if str(codes[pointer])[-4:-3] == '1':
                    input2_mode = 1

                if input1_mode == 0:
                    input1 = codes[codes[pointer+1]]
                elif input1_mode == 1:
                    input1 = codes[pointer+1]

                if input2_mode == 0:
                    input2 = codes[codes[pointer+2]]
                elif input2_mode == 1:
                    input2 = codes[pointer+2]

                if input1 == input2:
                    codes[codes[pointer+3]] = 1
                else:
                    codes[codes[pointer+3]] = 0

                pointer += 4

            elif opcode == '99':

                break

            else:
                print(f"An error code was encountered: opcode {codes[pointer]} "
                      f"at position {pointer}")
                pointer += (len(codes) - pointer)

        return outputs


def run_intcode(program, input):
    intcode = RunIntcode(program, input)
    results = intcode.run_program()
    print(results)
    # print(run_intcode.codes)
    # print(run_intcode.temp_codes)
    # run_intcode.run_noun_verb()
    # print(run_intcode.experimental_codes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Intcode computer solution options.')

    parser.add_argument('read_file_name', type=str, help="""
                        Required. Enter the path to the input file that you
                        would like to analyze.  The file should be a
                        plaintext file with each record on its own line.
                        """)
    parser.add_argument('input', type=int, help="""
                        Starting program input.""")
    args = parser.parse_args()
    program = return_file_contents(args.read_file_name)
    run_intcode(program, args.input)

# Part One:
# Part Two:

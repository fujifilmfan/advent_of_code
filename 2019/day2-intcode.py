#!/usr/bin/env python

import argparse
from copy import deepcopy

from file_ops import return_file_contents


class RunIntcode:
    
    def __init__(self, program):
        self.codes = [int(i) for i in program[0].split(',')]
        self.temp_codes = []
        self.experimental_codes = []
        self.noun_verb_output = 0
    
    def run_program(self, codes):
        
        frame = 0
        self.temp_codes = codes
        
        while self.temp_codes[frame] is not 99:
            
            if self.temp_codes[frame] == 1:
                input1 = self.temp_codes[frame+1]
                input2 = self.temp_codes[frame+2]
                output = self.temp_codes[frame+3]
                
                self.temp_codes[output] = self.temp_codes[input1] + self.temp_codes[input2]
                
                frame += 4
            
            elif self.temp_codes[frame] == 2:
                input1 = self.temp_codes[frame + 1]
                input2 = self.temp_codes[frame + 2]
                output = self.temp_codes[frame + 3]
    
                self.temp_codes[output] = self.temp_codes[input1] * self.temp_codes[input2]
                
                frame += 4
                
            else:
                print(f"An error code was encountered: {self.temp_codes[frame]} at frame {frame}")
                                
                break
                
        # self.temp_codes = []
    
    def run_noun_verb(self):
        
        for noun in range(0,100):
            for verb in range(0,100):
                self.experimental_codes = deepcopy(self.codes)
                # print(self.experimental_codes)
                self.experimental_codes[1] = noun
                # print(self.experimental_codes[1])
                self.experimental_codes[2] = verb
                # print(self.experimental_codes[2])
                
                self.run_program(self.experimental_codes)
                
                self.noun_verb_output = self.temp_codes[0]
                # print(self.noun_verb_output)
    
                self.temp_codes = []
                
                if self.noun_verb_output == 19690720:
                    print(f"Noun: {noun}; Verb: {verb}")
        
        
def run_intcode(program):
    run_intcode = RunIntcode(program)
    run_intcode.run_program(run_intcode.codes)
    print(run_intcode.codes)
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
    args = parser.parse_args()
    program = return_file_contents(args.read_file_name)
    run_intcode(program)

# Part One:
# 5482655
# Part Two:
# 4967

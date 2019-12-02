#!/usr/bin/env python

import argparse
from math import floor

from file_ops import return_file_contents


class FuelCalc:
    
    def __init__(self, module_masses):
        self.module_masses = module_masses
        self.fuel_for_modules = []
        self.fuel_for_modules_sum = 0
        self.fuel_for_fuel = []
        self.fuel_for_fuel_sum = 0
    
    @staticmethod
    def calculate_fuel_requirement(mass):
        fuel = (floor(int(mass) / 3)) - 2
        
        return fuel

    def sum_fuel_for_modules(self):
        
        for mass in self.module_masses:
            fuel = self.calculate_fuel_requirement(mass)
            if fuel > 0:
                self.fuel_for_modules.append(fuel)
        
        for fuel_req in self.fuel_for_modules:
            self.fuel_for_modules_sum += fuel_req
                    
    def sum_fuel_for_fuel(self):
        
        self.fuel_for_fuel = self.fuel_for_modules
        
        while len(self.fuel_for_fuel) > 0:
            fuel = self.fuel_for_fuel.pop(0)
            fuel_req = self.calculate_fuel_requirement(fuel)
            
            if fuel_req > 0:
                self.fuel_for_fuel_sum += fuel_req
                self.fuel_for_fuel.append(fuel_req)


def calculate_fuel_req(module_masses):
    fuel_req = FuelCalc(module_masses)
    fuel_req.sum_fuel_for_modules()
    fuel_req.sum_fuel_for_fuel()
    print(fuel_req.fuel_for_modules_sum + fuel_req.fuel_for_fuel_sum)
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Rocket equation solution options.')

    parser.add_argument('read_file_name', type=str, help="""
                        Required. Enter the path to the input file that you
                        would like to analyze.  The file should be a
                        plaintext file with each record on its own line.
                        """)
    args = parser.parse_args()
    module_masses = return_file_contents(args.read_file_name)
    calculate_fuel_req(module_masses)

# Part One
# 3198599
# Part Two
# 1596443

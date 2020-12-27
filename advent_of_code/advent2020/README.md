## Advent of Code 2020 Notes

### Running scripts
---
I've had an abnormally hard time getting imports to work as expected. The new answer at 
[ModuleNotFoundError when running script from Terminal](https://stackoverflow.com/questions/50745094/modulenotfounderror-when-running-script-from-terminal/50752488) 
got me over the hump.

I'll describe some ways to run `day1_report_repair.py` (as an example) an associated tests.  
The script uses the import syntax `import advent_of_code.file_ops as file_ops`, 
and the test file uses `from advent_of_code.advent2020 import day1_report_repair as report_repair`.

#### Terminal
From the project root:  
`$ python -m advent_of_code.advent2020.day1_report_repair 
~/code/problems/advent_of_code/advent_of_code/advent2020/day1_input.txt -s 3`  
`$ pytest`  

#### Pycharm
Script path: `.../advent_of_code/advent2020/day1_report_repair.py` (`...` represents the rest of my path)  
Parameters: `day_input.txt -s 3`  
Working directory: `.../advent_of_code/advent_of_code/advent2020`    
Note that the working directory can be changed to the project root if the file path parameter is made more specific.

Script path: `.../advent_of_code/.venv/bin/pytest`  
Working directory: `.../advent_of_code/tests/advent2020_tests`  

### Notes
---

#### Day 10
Example 1:
0  (0)			(0)
1  1			1
2  4			4
3  5
4  6
5  7			7
6  10			10
7  11
8  12			12
9  15			15
10 16			16
11 19			19
12 22           22
                ^required

can be dropped = (5, 6, 11)
2^3 = 8

Example 2:
0  (0)			(0)
1  1			
2  2			
3  3			
4  4			4
5  7			7
6  8
7  9
8  10
9  11			11
10 14			14
11 17			17
12 18
13 19
14 20			20
15 23			23
16 24
17 25			25
18 28			28
19 31			31
20 32
21 33
22 34
23 35			35
24 38			38
25 39			39
26 42			42
27 45			45
28 46
29 47
30 48
31 49			49
32 52           52
                ^required

can be dropped = (1, 2, 3, 8, 9, 10, 18, 19, 24, 32, 33, 34, 46, 47, 48)
need at least one = ((1, 2, 3), (8, 9, 10), (32, 33, 34), (46, 47, 48))
optional = ((18, 19), (24))

7 * 7 * 7 * 7 * 4 * 2

A gap of more than 3 makes at least one of the numbers in the gap required.  
In Example 2, those gaps are 0-4, 7-11, 31-35, and 45-49. Or, required numbers (at minimum) can be defined as those that are 3 away from an adjacent number, which are probably easier to find than gaps.

A gap of exactly 3 makes any numbers in the gap optional.  
In Example 2, those gaps are 17-20 and 23-25.

123
12
 23
1 3
1
 2
  3
cannot be all empty
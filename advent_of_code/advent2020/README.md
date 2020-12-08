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

Advent of Code 2018: Solution Notes
-----------------------------------
https://stackoverflow.com/questions/46513358/finding-the-first-duplicate-of-an-array/46513425

[Day 1: Chronal Calibration](#day-1-chronal-calibration)  
[Day 2: Inventory Management System](#day-2-inventory-managementsystem)  

### Day 1: Chronal Calibration

#### What I learned
* a Python **set()** is an unordered collection of unique elements  
* **itertools.cycle()** is used to create an infinite iterator  

#### Usage notes
* `$ day1-chronal_calibration.py day1-input.txt -d`  
* `$ day1-chronal_calibration.py day1-input.txt -s`  
* `$ day1-chronal_calibration.py day1-input.txt -sd`  
* `$ day1-chronal_calibration.py --help`:  
```
usage: day1-chronal_calibration.py [-h] [-d] [-s] read_file_name

Frequency processing options.

positional arguments:
  read_file_name        Required. Enter the path to the frequency changes file
                        that you would like analyze. The file should be a
                        plaintext file with each frequency change on its own
                        line.

optional arguments:
  -h, --help            show this help message and exit
  -d, --find_first_duplicate
                        Find first duplicate frequency.
  -s, --sum_frequencies
                        Sum the frequency changes in the input file
```
* `$ day1-chronal_calibration.py day1-input.txt`:
```
Use the -s or -d flag to see the frequency sum or first duplicate, respectively.
```

### Day 2: Inventory Management System

#### What I learned
* **collections.Counter()** is used to store elements as dictionary keys with their counts as dictionary values  
* **zip()** is used to return an iterator of tuples; maps similar index of multiple containers  
* good review of nested while loops  

#### Usage notes
* `$ day2-inventory_management.py day2-input.txt`  
```
checksum: 4980
common letters: qysdtrkloagnfozuwujmhrbvx
```
Advent of Code 2018: Solution Notes
-----------------------------------

[Day 1: Chronal Calibration](#day-1-chronal-calibration)  
[Day 2: Inventory Management System](#day-2-inventory-management-system)  
[Day 3: No Matter How You Slice It](#day-3-no-matter-how-you-slice-it)  

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
* I don't need to make a list of each letter in the alphabet; things like that can often be found in a module (in this case, string.ascii_lowercase)
* good review of nested while loops  
* on that subject, I can replace:  
```
    i = 0
    while i < len(self.box_ids) - 1:
        j = 1
        while j < len(self.box_ids):
            <CODE TO EXECUTE>
            j += 1
        i += 1
```
with:  
```
    for i in range(len(self.box_ids)):
        for j in range(len(self.box_ids)):
            <CODE TO EXECUTE>
```
or:
```
    for i, _ in enumerate(self.box_ids):
        for j, _ in enumerate(self.box_ids):
            <CODE TO EXECUTE>
```
Thank you, Ryan!  

#### Usage notes
* `$ day2-inventory_management.py day2-input.txt`  
```
checksum: 4980
common letters: qysdtrkloagnfozuwujmhrbvx
```

### Day 3: No Matter How You Slice It

#### What I learned
* how to use **split()** and **replace()** (I opted not to use regex, such as `@\W(\d)+,(\d)+:\W(\d)+x(\d)+`, in order to learn a different way to do things); helpful: [Split Strings with Multiple Delimiters?](https://stackoverflow.com/questions/1059559/split-strings-with-multiple-delimiters/1059601)
* **itertools.product()** is used to make a cartesian product (equivalent to a nested for-loop); particularly helpful: [Python merging two lists with all possible permutations](https://stackoverflow.com/questions/32438350/python-merging-two-lists-with-all-possible-permutations)
* using **any** and **all** (in addition to iterables, generators, etc.) from [Check Whether All Items Match a Condition in Python](https://treyhunner.com/2016/11/check-whether-all-items-match-a-condition-in-python/)

#### Usage notes
* `$ day3-fabric_slicing.py day3-input.txt`  
```
Number of square inches claimed once: 365706
Number of square inches claimed more than once: 121259
Non-overlapping claim IDs: ['239']
```

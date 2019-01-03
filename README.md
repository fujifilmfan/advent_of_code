Advent of Code 2018
-----

### Usage Notes

#### Day 1: Chronal Calibration
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


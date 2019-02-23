#!/usr/bin/env python

import argparse
import re
from collections import Counter

from file_ops import return_file_contents


class Records(object):

    def __init__(self, guard_records):
        self.records = guard_records
        self.sorted_records = []
        self.guard_records = {}
        self.minutes_asleep = {}
        self.search_pattern = re.compile('\d{4}-\d{2}-\d{2}\W\d{2}:\d{2}')

    def process_records(self):
        self.sort_records()
        self.create_guard_record_dict()
        self.find_total_minutes_asleep()

    def sort_records(self):
        """Sort guard repose records by timestamp."""
        # the lambda function and regex is actually unnecessary here; sorted() will work fine
        # self.sorted_records = sorted(self.records, key=lambda r: re.findall(self.search_pattern, r))
        # list.sort() does not work since self.records is not yet a list
        self.sorted_records = sorted(self.records)

    def create_guard_record_dict(self):
        """Create guard record dictionary in the following format:
            guard_records = {
                2371: {'1518-11-20 23:57': []},
                3109: {'1518-11-22 00:01': [],
                       '1518-11-22 23:59': []}
            }
        """
        guard_on_duty = 0
        for record in self.sorted_records:
            if "Guard" in record:
                # guard_on_duty = 0
                # the slice [26:-14] gets just the guard ID, e.g. 709 or 1811; the ID is the only variable-length
                # part of the record line; this is to keep track of which guard is on duty at any time
                guard_on_duty = record[26:-14]
                # the slice [1:17] gives the timestamp of the start time
                guard_start_time = record[1:17]
                # Create a guard ID key in the guard_records dictionary if it's not already there
                if guard_on_duty not in self.guard_records:
                    self.guard_records[guard_on_duty] = {}
                # Create a shift time start key in the guard ID sub-dictionary if it's not already there
                if guard_start_time not in self.guard_records[guard_on_duty]:
                    self.guard_records[guard_on_duty][guard_start_time] = []
            else:
                # the slice [15:17] gets the double-digit minute of the record
                minute = int(record[15:17])
                if "falls" in record:
                    last_sleep = minute
                elif "wakes" in record:
                    last_wake = minute
                    # Add the minutes asleep to a list linked to the guard's start time
                    self.guard_records[guard_on_duty][guard_start_time].extend(list(range(last_sleep, last_wake)))

    def find_total_minutes_asleep(self):
        for guard in self.guard_records:
            self.minutes_asleep[guard] = {}
            total_minutes_asleep = 0
            all_the_minutes_asleep = []
            for shift in self.guard_records[guard]:
                self.minutes_asleep[guard]['frequency'] = {}
                for minute in self.guard_records[guard][shift]:
                    all_the_minutes_asleep.extend([minute])
                total_minutes_asleep += len(self.guard_records[guard][shift])
            self.minutes_asleep[guard]['frequency'] = dict(Counter(all_the_minutes_asleep))
            self.minutes_asleep[guard]['total'] = total_minutes_asleep
        return self.minutes_asleep

    def find_sleepiest_guard_by_total(self):
        sleepiest_guard = max(self.minutes_asleep.keys(), key=(lambda k: self.minutes_asleep[k]['total']))
        sleepiest_minute = int(self.find_sleepiest_minute(sleepiest_guard)[0])
        value = int(sleepiest_guard) * sleepiest_minute
        print('Guard #{id}: {sleep} minutes total, {minute} sleepiest minute, value: {value}'.format(
            id=sleepiest_guard,
            sleep=str(self.minutes_asleep[sleepiest_guard]['total']),
            minute=str(sleepiest_minute),
            value=str(value)))

    def find_sleepiest_guard_by_minute(self):
        sleepiest_minutes = {}
        for guard in self.guard_records:
            sleepiest_minutes[guard] = self.find_sleepiest_minute(guard)
        sleepiest_guard = max(sleepiest_minutes.keys(), key=(lambda k: sleepiest_minutes[k][1]))
        value = int(sleepiest_guard) * sleepiest_minutes[sleepiest_guard][0]
        print('Guard #{id}: {minute} sleepiest minute, frequency: {frequency}, value: {value}'.format(
            id=sleepiest_guard,
            minute=sleepiest_minutes[sleepiest_guard][0],
            frequency=sleepiest_minutes[sleepiest_guard][1],
            value=str(value)))

    def find_sleepiest_minute(self, guard):
        try:
            sleepiest_minute = max(self.minutes_asleep[guard]['frequency'], key=(lambda k: self.minutes_asleep[
                guard]['frequency'][k]))
            return[sleepiest_minute, self.minutes_asleep[guard]['frequency'][sleepiest_minute]]
        except ValueError:
            return[0, 0]


def analyze_records(guard_records):
    records = Records(guard_records)
    records.process_records()
    records.find_sleepiest_guard_by_total()
    records.find_sleepiest_guard_by_minute()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Guard records processing options.')

    parser.add_argument('read_file_name', type=str, help="""
                        Required. Enter the path to the input file that you
                        would like to analyze.  The file should be a
                        plaintext file with each record on its own line.
                        """)
    args = parser.parse_args()
    guard_records = return_file_contents(args.read_file_name)
    # print(guard_records)
    analyze_records(guard_records)

# Output:
# Guard #73: 461 minutes total, 44 sleepiest minute, value: 3212
# Guard #191: 26 sleepiest minute, frequency: 17, value: 4966

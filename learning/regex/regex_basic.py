__author__ = 'wccalvin'

import re

file_obj = open('example.txt', 'r')

for line in file_obj:
    line = line.strip()
    if re.search(r'^X.*', line):  # ^X -> start with X; . -> any character; * -> any number of times
        print(line)

file_obj.close()

regex_basic.py
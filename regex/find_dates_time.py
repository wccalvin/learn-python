#!/usr/bin/env python

import re

file_obj = open('date_time_values.txt', 'r')

for line in file_obj:
    line = line.strip()
    if re.search(r'.*:', line):  # Match anything with : on the line
        print(line)              # We can also do it without the .* in it.

file_obj.close()

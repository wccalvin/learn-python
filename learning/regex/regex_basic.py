import re

file_obj = open('example.txt', 'r')

for line in file_obj:
    line = line.strip()
    # ^X -> start with X; . -> any character; * -> any number of times
    if re.search(r'^X.*', line):
        print(line)

file_obj.close()

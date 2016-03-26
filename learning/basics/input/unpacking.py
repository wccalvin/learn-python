#!/usr/bin/env python

from sys import argv
from sys import exit

parse_all = argv

print("Given command args: {}".format(parse_all))

if len(parse_all) < 5:
    print("Not enough values to parse and print.")
    exit(1)

(one, two, three, four, five) = parse_all

print("First: {}".format(one))
print("Second: {}".format(two))
print("Third: {}".format(three))
print("Fourth: {}".format(four))
print("Fifth: {}".format(five))

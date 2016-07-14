#!/usr/bin/env python

from sys import argv

parse_all = argv
index = 0
while index < len(parse_all):
    print("{} argument: {}".format(str(index + 1),
                                   parse_all[index]))
    index += 1

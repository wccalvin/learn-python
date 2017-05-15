#!/usr/bin/env python3
"""
Using replace to translate few alphabets to numbers
"""

import sys

try:
    my_input = input("Enter some text: ")
except KeyboardInterrupt:
    print("User aborted.")
    sys.exit(1)

rp_a = my_input.replace('a', str(4))
rp_b = rp_a.replace('b', str(8))
rp_e = rp_b.replace('e', str(3))
rp_l = rp_e.replace('l', str(1))
rp_o = rp_l.replace('o', str(0))
rp_s = rp_o.replace('s', str(5))
rp_t = rp_s.replace('t', str(7))

print(rp_t)

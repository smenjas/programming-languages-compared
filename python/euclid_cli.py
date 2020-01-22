#!/usr/bin/env python3

import os
import sys
from euclid import euclid

if len(sys.argv) < 3:
    filename = os.path.basename(__file__)
    print("usage: {0} <first-number> <second-number>".format(filename))
    exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])

result = euclid(x, y)
print(result)

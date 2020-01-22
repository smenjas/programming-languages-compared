#!/usr/bin/env python3

import os
import sys
from factorial import factorial

if len(sys.argv) < 2:
    filename = os.path.basename(__file__)
    print("usage: {0} <natural-number>".format(filename))
    exit(1)

n = int(sys.argv[1])

result = factorial(n)
print(result)

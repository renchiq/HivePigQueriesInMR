#!/usr/bin/python3

import sys

for line in sys.stdin:
    name, surname = line.strip().split('\t')

    print('{}\t{}'.format(name, surname))

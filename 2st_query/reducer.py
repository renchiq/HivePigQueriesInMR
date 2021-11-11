#!/usr/bin/python3

import sys

for line in sys.stdin:
    name, surname, city = line.strip().split('\t')

    if city == 'Moscow':
        print('{}\t{}\t{}'.format(name, surname, city))
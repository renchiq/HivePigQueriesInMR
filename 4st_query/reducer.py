#!/usr/bin/python3
# select name, surname
# from workers
# where name like 'M%' or name like 'H%';

import sys

for line in sys.stdin:
    name, surname = line.strip().split('\t')
    if str(name).startswith(('M', 'H')):
        print('{}\t{}'.format(name, surname))

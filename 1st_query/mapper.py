#!/usr/bin/python3
# select name, surname
# from workers;

import sys

for line in sys.stdin:
    worker_info = line.strip().split(',')

    print('{0}\t{1}'.format(worker_info[1], worker_info[2]))

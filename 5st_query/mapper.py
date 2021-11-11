#!/usr/bin/python3
# select workers.name, workers.surname, posts.name, posts.descr
# from workers
# join posts on workers.post_id == posts.id;

import sys

for line in sys.stdin:
    line = line.strip().split(',')

    if len(line) == 6:
        print('{0}\tworker\t{1}\t{2}'.format(line[4], line[1], line[2]))
    elif len(line) == 3:
        print('{0}\tpost\t{1}\t{2}'.format(line[0], line[1], line[2]))
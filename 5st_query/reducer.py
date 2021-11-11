#!/usr/bin/python3
# select workers.name, workers.surname, posts.name, posts.descr
# from workers
# join posts on workers.post_id == posts.id;

import sys

last_key = None
H = dict()

for line in sys.stdin:
    key, tag, name, optional = line.strip().split('\t')

    if last_key is None or last_key == key:
        last_key = key
        if tag == 'post':
            H[tag] = [name, optional]
        if tag == 'worker':
            if tag in H:
                H[tag].append([name, optional])
            else:
                H[tag] = [[name, optional]]
    else:
        for worker in H['worker']:
            if 'post' in H:
                print('{0}\t{1}\t{2}'.format(worker[0], worker[1], '\t'.join(H['post'])))
        H.clear()
        last_key = key
        if tag == 'post':
            H[tag] = [name, optional]
        elif tag == 'worker':
            H[tag] = [[name, optional]]

if last_key:
    for worker in H['worker']:
        print('{0}\t{1}\t{2}'.format(worker[0], worker[1], '\t'.join(H['post'])))
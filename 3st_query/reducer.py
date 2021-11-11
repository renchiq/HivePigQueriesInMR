#!/usr/bin/python3
# select workers.name, workers.surname, departments.name, departments.descr
# from workers
# left join departments on workers.department_id == departments.id;

import sys

last_key = None
H = dict()

for line in sys.stdin:
    f = open('/home/renchiq-centos/mysources/DataProcessing/3st_query/shuffle.txt', 'a')
    f.write(line)
    f.close()
    key, tag, name, optional = line.strip().split('\t')

    if last_key is None or last_key == key:
        last_key = key
        if tag == 'department':
            H[tag] = [name, optional]
        if tag == 'worker':
            if tag in H:
                H[tag].append([name, optional])
            else:
                H[tag] = [[name, optional]]
    else:
        for worker in H['worker']:
            if 'department' in H:
                print('{0}\t{1}\t{2}'.format(worker[0], worker[1], '\t'.join(H['department'])))
            else:
                print('{0}\t{1}\tnull\tnull'.format(worker[0], worker[1]))
        H.clear()
        last_key = key
        if tag == 'department':
            H[tag] = [name, optional]
        elif tag == 'worker':
            H[tag] = [[name, optional]]

if last_key:
    for worker in H['worker']:
        print('{0}\t{1}\t{2}'.format(worker[0], worker[1], '\t'.join(H['department'])))

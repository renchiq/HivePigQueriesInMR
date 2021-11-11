#!/usr/bin/python3
# select workers.name, workers.surname, departments.name, departments.descr
# from workers
# left join departments on workers.department_id == departments.id;

import sys

for line in sys.stdin:
    f = open('/home/renchiq-centos/mysources/DataProcessing/3st_query/to_mapper.txt', 'a')
    f.write(line)
    f.close()
    line = line.strip().split(',')

    if len(line) == 6:
        print('{0}\tworker\t{1}\t{2}'.format(line[5], line[1], line[2]))
    elif len(line) == 3:
        print('{0}\tdepartment\t{1}\t{2}'.format(line[0], line[1], line[2]))
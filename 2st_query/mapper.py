# select name,surname,city
# from workers
# where city == 'Moscow';

import sys

for line in sys.stdin:
    worker_info = line.strip().split(',')

    print('{0}\t{1}\t{2}'.format(worker_info[1], worker_info[2], worker_info[3]))
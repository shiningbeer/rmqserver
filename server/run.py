#!/usr/bin/env python
import os

from time import sleep
while True:
    os.system('python dispatch_task.py')
    print '-'
    os.system('python collect_progress.py')
    for i in range(3):
        print '-'
    sleep(3)
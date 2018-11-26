#!/usr/bin/env python
import os

import sys
sys.path.append('..')
from util.cprint import cprint
import datetime
from time import sleep
while True:
    cprint (datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S'),'SKYBLUE')
    os.system('python dispatch_cidr_task.py')
    print ' '
    os.system('python collect_cidr_progress.py')
    for i in range(3):
        print ' '
    sleep(10)
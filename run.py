#!/usr/bin/env python
import os

import sys
# sys.path.append('..')
from util.cprint import cprint
import datetime
from time import sleep
while True:
    cprint (datetime.datetime.now().strftime('%Y.%m.%d %H:%M:%S'),'cyan')
    os.system('python cidr_dispatch.py')
    print(' ')
    os.system('python cidr_progress.py')
    print(' ')
    os.system('python ipv4_dispatch.py')
    print(' ')
    os.system('python ipv4_progress.py')
    for i in range(3):
        print(' ')
    sleep(10)
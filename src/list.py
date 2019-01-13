#!/usr/bin/env python

import sys
# sys.path.append('..')
from util.config import Config
from util.cprint import cprint
from util.dao import Dao
# read config
config=Config('./util/config.ini')
# connect to db of cidr task
dao_cidr=Dao(config.db_host,config.db_port,config.db_cidr)
dao_ipv4=Dao(config.db_host,config.db_port,config.db_ipv4)

cidr_tasks=dao_cidr.find_many(config.col_taskinfo,{})
cidr_tasks_count=dao_cidr.find_count(config.col_taskinfo,{})
ipv4_tasks=dao_ipv4.find_many(config.col_taskinfo,{})
ipv4_tasks_count=dao_ipv4.find_count(config.col_taskinfo,{})
cprint('------cidr tasks-----','magenta')
if cidr_tasks_count==0:
    print('None')
else:
    cprint ('name       port       progress       pause   ','cyan')
    for task in cidr_tasks:
        print(task['name'],'     ',task['port'],'     ','%d/%d'%(task['progress'],task['count']),'     ',task['pause'])
cprint ('------ipv4 tasks-----','yellow')

if ipv4_tasks_count==0:
    print('None')
else:
    cprint ('name       plugin      port      progress       pause      error     ','cyan')
    for task in ipv4_tasks:
        print(task['name'],'     ',task['plugin'],'     ',task['port'],'     ','%d/%d'%(task['progress'],task['count']),'     ',task['pause'],'     ',task['error'])

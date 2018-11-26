#!/usr/bin/env python

import sys
sys.path.append('..')
from util.config import Config
from util.cprint import cprint
from util.dao import Dao
# read config
config=Config('../util/config.ini')
# connect to db of cidr task
dao_cidr=Dao(config.db_host,config.db_port,config.db_cidr)
dao_plugin=Dao(config.db_host,config.db_port,config.db_plugin)

cidr_tasks=dao_cidr.find_many(config.col_taskinfo,{})
plugin_tasks=dao_plugin.find_many(config.col_taskinfo,{})
cprint(u'------cidr tasks-----','PINK')
if cidr_tasks.count()==0:
    print 'None'
else:
    cprint ('name       port       progress       pause   ','SKYBLUE')
    for task in cidr_tasks:
        print task['name'],'     ',task['port'],'     ','%d/%d'%(task['progress'],task['count']),'     ',task['pause']
cprint (u'------plugin tasks-----','RED')

if plugin_tasks.count()==0:
    print 'None'
else:
    cprint ('name       plugin      port      progress       pause      error     ','SKYBLUE')
    for task in plugin_tasks:
        print task['name'],'     ',task['plugin'],'     ',task['port'],'     ','%d/%d'%(task['progress'],task['count']),'     ',task['pause'],'     ',task['error']

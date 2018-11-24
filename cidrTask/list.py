#!/usr/bin/env python

import sys
sys.path.append('..')
from util.config import Config
from util.dao import Dao
from util.functions import is_cidr,is_ipv4
# read config
config=Config('../util/config.ini')
# connect to db of cidr task
dao_cidr=Dao(config.db_host,config.db_port,config.db_cidr)
dao_plugin=Dao(config.db_host,config.db_port,config.db_plugin)

cidr_tasks=dao_cidr.find_many(config.col_taskinfo,{})
plugin_tasks=dao_plugin.find_many(config.col_taskinfo,{})
print u'------cidr tasks-----'
if cidr_tasks.count()==0:
    print 'None'
else:
    print 'name      ','port   ','progress   ','pause   '
    for task in cidr_tasks:
        print task['name'],'     ',task['port'],'     ','%d/%d'%(task['progress'],task['count']),'     ',task['pause']
print u'------plugin tasks-----'

if plugin_tasks.count()==0:
    print 'None'
else:
    for task in plugin_tasks:
        print task

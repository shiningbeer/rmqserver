#!/usr/bin/env python

import sys
sys.path.append('..')
from util.config import Config
from util.dao import Dao
from util.functions import is_cidr,is_ipv4
# read config
config=Config('../util/config.ini')
# connect to db of cidr task
dao=Dao(config.db_host,config.db_port,config.db_cidr)
if len(sys.argv)==1:
    if raw_input('Do you want to delete all the cidr tasks? (y/n)')!='y':
        sys.exit(0)
    tasks=dao.find_many(config.col_taskinfo,{})
    for task in tasks:
        dao.drop_col(task['name'])
    dao.delete_many(config.col_taskinfo,{})
    print u'All cidr tasks are deleted!'
else:
    name= sys.argv[1]

    if not dao.collection_exits(name):
        print u'task name not exists!'
        sys.exit(0)
    else:
        dao.delete_one(config.col_taskinfo,{'name':name})
        dao.drop_col(name)
        print u'Task %s deleted successfully!' % name
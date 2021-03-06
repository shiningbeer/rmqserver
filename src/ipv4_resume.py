#!/usr/bin/env python

import sys
# sys.path.append('..')
from util.config import Config
from util.dao import Dao
# read config
config=Config('./util/config.ini')
# connect to db of ipv4 task
dao=Dao(config.db_host,config.db_port,config.db_ipv4)
if len(sys.argv)==1:
    if input('Do you want to resume all the ipv4 tasks? (y/n)')!='y':
        sys.exit(0)
    dao.update_many(config.col_taskinfo,{},{'pause':False})
    print('All ipv4 tasks are resumed!')
else:
    name= sys.argv[1]

    if not dao.collection_exits(name):
        print('task name not exists!')
        sys.exit(0)
    else:
        dao.update_one(config.col_taskinfo,{'name':name},{'pause':False})
        print('Task %s resume successfully!' % name)
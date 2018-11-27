#!/usr/bin/env python

import sys
# sys.path.append('..')
from util.config import Config
from util.cprint import cprint
from util.dao import Dao
cprint ('------CIDR Task Progress Info--------','magenta')
# read config
config=Config('./util/config.ini')
# connect to db of cidr task
dao=Dao(config.db_host,config.db_port,config.db_cidr)
# collect progress
uncompleted_tasks=dao.find_many(config.col_taskinfo,{'complete':False})
if uncompleted_tasks.count()==0:
    print 'task all complete!'
for utask in uncompleted_tasks:
    finished_count=dao.find_count(utask['name'],{'$or':[{'error':{'$exists':True}},{'result':{'$exists':True}}]})
    sent_count=dao.find_count(utask['name'],{'sent':True})
    if finished_count==utask['count']:
        #complete
        dao.update_one(config.col_taskinfo,{'_id':utask['_id']},{'complete':True})
    dao.update_one(config.col_taskinfo,{'_id':utask['_id']},{'progress':finished_count})
    print 'task--%s : sent (%d/%d)   complete (%d/%d)' % (utask['name'],sent_count,utask['count'], finished_count,utask['count'])
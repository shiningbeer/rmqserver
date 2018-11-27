#!/usr/bin/env python

import sys
sys.path.append('..')
from util.cprint import cprint
from util.config import Config
from util.dao import Dao
cprint ('------ipv4 Task Progress Info--------','yellow')
# read config
config=Config('./util/config.ini')
# connect to db of ipv4 task
dao=Dao(config.db_host,config.db_port,config.db_ipv4)
# collect progress
uncompleted_tasks=dao.find_many(config.col_taskinfo,{'complete':False})
if uncompleted_tasks.count()==0:
    print 'task all complete!'
for utask in uncompleted_tasks:
    finished_count=dao.find_count(utask['name'],{'$or':[{'error':{'$exists':True}},{'result':{'$exists':True}}]})
    error_count=dao.find_count(utask['name'],{'error':{'$exists':True}})
    sent_count=dao.find_count(utask['name'],{'sent':True})
    if finished_count==utask['count']:
        #complete
        dao.update_one(config.col_taskinfo,{'_id':utask['_id']},{'complete':True})
    dao.update_one(config.col_taskinfo,{'_id':utask['_id']},{'progress':finished_count})
    print '%s: sent(%d/%d) complete(%d/%d) error(%d)' % (utask['name'],sent_count,utask['count'], finished_count,utask['count'],error_count)
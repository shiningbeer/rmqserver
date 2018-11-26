#!/usr/bin/env python

import sys
sys.path.append('..')
from util.config import Config
from util.dao import Dao
# read config
config=Config('../util/config.ini')
# connect to db of cidr task
dao=Dao(config.db_host,config.db_port,config.db_cidr)
if len(sys.argv)!=2:
    print u'sys args wrong!'
    sys.exit(0)
task_name=sys.argv[1]
if not dao.collection_exits(task_name):
    print u'task does not exit!'
    sys.exit(0)
items=dao.find_many(task_name,{'result':{'$exists':True}})
result_list=[]
for item in items:
    rlist=item['result']
    result_list.extend(rlist)
f=open(task_name+'.ret','w')
for i in range(len(result_list)-1):
    result_list[i]+='\n'
f.writelines(result_list)
f.close()
print u'task result exported successfully!'
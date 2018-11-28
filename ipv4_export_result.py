#!/usr/bin/env python

import sys
# sys.path.append('..')
from util.config import Config
from util.dao import Dao
import json
# read config
config=Config('./util/config.ini')
# connect to db of ipv4 task
dao=Dao(config.db_host,config.db_port,config.db_ipv4)
if len(sys.argv)!=2:
    print u'sys args wrong!'
    sys.exit(0)
task_name=sys.argv[1]
if not dao.collection_exits(task_name):
    print u'task does not exit!'
    sys.exit(0)
items=dao.find_many(task_name,{'result':{'$exists':True}})

f=open(task_name+'.irt','w')
for item in items:
    if item['result']!=None and item['result']!={}:
        item.pop('sent')
        item.pop('_id')
        itemstr=json.dumps(item)
        f.write(itemstr)
        f.write('\n')

f.close()
print u'task result exported successfully!'
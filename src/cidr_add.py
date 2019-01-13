#!/usr/bin/env python

import sys
# sys.path.append('..')
from util.config import Config
from util.dao import Dao
from util.functions import is_cidr
# read config
config=Config('./util/config.ini')
# connect to db of cidr task
dao=Dao(config.db_host,config.db_port,config.db_cidr)
# parse sys argv
try:
    index=sys.argv.index('-n')
    name=sys.argv[index+1] # todo: task name should not be start with '-'
    if name.startswith('-'):
        print ('task name should not begin with -')
        sys.exit(0)
    index=sys.argv.index('-p')
    port=int(sys.argv[index+1])
    index=sys.argv.index('-t')
    target=sys.argv[index+1]
except Exception as e:
    print('sys args wrong!',repr(e))
    sys.exit(0)
if dao.collection_exits(name):
    print('task name exists, please change to another name!')
    sys.exit(0)
try:
    f=open(target,'r')
except Exception as e:
    print('cannot open the target file!',repr(e))
    sys.exit(0)

# examine cidr format of the lines in the target file
line_number=0
for line in f:
    line_number+=1
    if not is_cidr(line):
        print(('tartget file contains none-cidr format at line : %s' % line_number))
        sys.exit(0)
# everything is ok, add the task to db
f.seek(0)
total=line_number
line_number=0
for line in f:
    line_number+=1
    doc={'ip':line.strip(),'port':port}
    x=dao.insert_one(name,doc)
    print('progress:%d/%d' % (line_number,total),end='\r')
    if line_number==total:
        print('progress:%d/%d' % (line_number,total),end='\n')

paused=False
if '-pause' in sys.argv:
    paused=True

new_task={'name':name,'port':port,'complete':False,'pause':paused,'allSent':False,'count':line_number,'progress':0}
dao.insert_one(config.col_taskinfo,new_task)
print('add task successful!')
f.close()

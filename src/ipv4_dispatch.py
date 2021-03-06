#!/usr/bin/env python
import sys
# sys.path.append('..')
from util.sender import Sender
from util.logger import logger
from util.dao import Dao
import json
from util.config import Config
from util.cprint import cprint


cprint ('------IPV4 Task Dispatch Info--------','yellow')
# read config
config=Config('./util/config.ini')
# connect to db of ipv4 task
dao=Dao(config.db_host,config.db_port,config.db_ipv4)

try:
    send=Sender(config.rmq_host,config.rmq_user,config.rmq_password,config.ipv4_task_channel)
except Exception as e:
    print('cannot connect rmq server!',repr(e))
    sys.exit(0)
msg_count=send.get_msg_count()
if msg_count>config.ipv4_max_length:
    print('queue length: %s > %s. waiting...' % (msg_count, config.ipv4_max_length))
    sys.exit(0)
print('queue length: %d ' % msg_count)
task=dao.find_one(config.col_taskinfo,{'allSent':False,'pause':False})
if task is None:
    ptasks=dao.find_many(config.col_taskinfo,{'pause':True})
    ptasks_count=dao.find_count(config.col_taskinfo,{'pause':True})
    if ptasks_count==0:
        print('no task now!')

    else:
        for pt in ptasks:
            print('%s: paused.' % pt['name'])
    sys.exit(0)
col_name=task['name']
task_id=task['_id']
if not dao.collection_exits(col_name):
    logger.critical('the task %s listed in the taskInfo table is missing its collection!' % col_name)
    dao.delete_many(config.col_taskinfo,{'name':col_name})
    logger.critical('the task %s is deleted in tasinInfo table!' % col_name)
    sys.exit(0)
for i in range(config.ipv4_batch_count):
    doc=dao.find_one(col_name,{'sent':None})
    if doc is None:
        # means the ip of task is all sent
        dao.update_many(config.col_taskinfo,{'_id':task_id},{'allSent':True})
        sys.exit(0)
    doc['name']=col_name
    doc_id=doc['_id']
    doc['_id']=str(doc['_id'])
    msg=json.dumps(doc)
    try:
        send.send_msg(msg)
    except Exception as e:
        print(repr(e))
        continue
    dao.update_one(col_name,{'_id':doc_id},{'sent':True})
print('task--%s : sent another %d' % (col_name,config.ipv4_batch_count))
send.close()
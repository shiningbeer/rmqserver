#!/usr/bin/env python
import sys
sys.path.append('..')
from util.cprint import lprint
from util.sender import Sender
from util.logger import logger
from util.receiver import Receiver
from util.dao import Dao
import json
import os
from bson import ObjectId
from time import sleep
import datetime
from threading import Thread

from util.config import Config
try:
    if len(sys.argv)==1:
        run_count=1
    else:
        run_count=int(sys.argv[1])
except Exception,e:
    print u'sys args wrong!',repr(e)
    sys.exit(0)
# read config
config=Config('../util/config.ini')
# connect to db of plugin task
dao=Dao(config.db_host,config.db_port,config.db_plugin)
def deal_with_msg(body):
    try:
        task=json.loads(body)    
        id=task['_id']
        name=task['name']
        msg=task['msg']
    except Exception, e:
        logger.error('%s, original message: %s' %(repr(e),body))
        return
    if id is None or name is None:
        logger.error('failed messge, original message: %s' % body)
        return
    try:
        oid=ObjectId(id)
    except Exception,e:
        logger.error('%s, original message: %s' %(repr(e),body))
        return
    dao.update_one(name,{'_id':oid},msg)
    lprint(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),'SKYBLUE')
    print u'-- stored a result of task: %s' % name
try:
    for i in range(run_count):
        receive=Receiver(config.rmq_host,config.rmq_user,config.rmq_password,config.plugin_result_channel,deal_with_msg)
        t=Thread(target=receive.start_listen).start()
except Exception,e:
    print u'cannot connect rmq server!',repr(e)
    sys.exit(0)

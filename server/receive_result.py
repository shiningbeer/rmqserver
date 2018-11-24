#!/usr/bin/env python
import sys
sys.path.append('..')
from util.sender import Sender
from util.logger import logger
from util.receiver import Receiver
from util.dao import Dao
import json
import os
from bson import ObjectId
from time import sleep

from util.config import Config

# read config
config=Config('../util/config.ini')
# connect to db of cidr task
dao=Dao(config.db_host,config.db_port,config.db_cidr)
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
    print u'received and stored a result item of task: %s' % name
try:
    receive=Receiver(config.rmq_host,config.rmq_user,config.rmq_password,config.cidr_receive_channel,deal_with_msg)
    receive.start_listen()
except Exception,e:
    print u'cannot connect rmq server!',repr(e)
    sys.exit(0)

#!/usr/bin/env python
import sys
# sys.path.append('..')
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
        run_cidr_count=1
        run_ipv4_count=2
    else:
        index=sys.argv.index('-c')
        run_cidr_count=int(sys.argv[index+1])
        index=sys.argv.index('-p')
        run_ipv4_count=int(sys.argv[index+1])
except Exception as e:
    print('sys args wrong!',repr(e))
    sys.exit(0)
# read config
config=Config('./util/config.ini')
# connect to db of ipv4 task
dao_ipv4=Dao(config.db_host,config.db_port,config.db_ipv4)
dao_cidr=Dao(config.db_host,config.db_port,config.db_cidr)
def deal_with_ipv4(body):
    try:
        task=json.loads(body)    
        id=task['_id']
        name=task['name']
        msg=task['msg']
    except Exception as e:
        logger.error('%s, original message: %s' %(repr(e),body))
        return
    if id is None or name is None:
        logger.error('failed messge, original message: %s' % body)
        return
    try:
        oid=ObjectId(id)
    except Exception as e:
        logger.error('%s, original message: %s' %(repr(e),body))
        return
    dao_ipv4.update_one(name,{'_id':oid},msg)
    lprint(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),'cyan')
    lprint('ipv4','yellow')
    print('-- stored a result of task: %s' % name)

def deal_with_cidr(body):
    try:
        task=json.loads(body)    
        id=task['_id']
        name=task['name']
        msg=task['msg']
    except Exception as e:
        logger.error('%s, original message: %s' %(repr(e),body))
        return
    if id is None or name is None:
        logger.error('failed messge, original message: %s' % body)
        return
    try:
        oid=ObjectId(id)
    except Exception as e:
        logger.error('%s, original message: %s' %(repr(e),body))
        return
    dao_cidr.update_one(name,{'_id':oid},msg)
    lprint(datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'),'cyan')
    lprint('cidr','magenta')
    print('-- stored a result of task: %s' % name)
try:
    for i in range(run_ipv4_count):
        receive=Receiver(config.rmq_host,config.rmq_user,config.rmq_password,config.ipv4_result_channel,deal_with_ipv4)
        t=Thread(target=receive.start_listen).start()
    for i in range(run_cidr_count):
        receive=Receiver(config.rmq_host,config.rmq_user,config.rmq_password,config.cidr_result_channel,deal_with_cidr)
        receive.start_listen()
except Exception as e:
    print('cannot connect rmq server!',repr(e))
    sys.exit(0)

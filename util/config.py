import ConfigParser
import sys

class Config():
    def __init__(self,file):
        try:
            config=ConfigParser.ConfigParser()
            config.read(file)
            self.rmq_host=config.get('rmq','host')
            self.rmq_user=config.get('rmq','user')
            self.rmq_password=config.get('rmq','password')
            self.cidr_task_channel=config.get('rmq','cidr_task_channel')
            self.ipv4_task_channel=config.get('rmq','ipv4_task_channel')
            self.cidr_result_channel=config.get('rmq','cidr_result_channel')
            self.ipv4_result_channel=config.get('rmq','ipv4_result_channel')
            self.cidr_max_length=int(config.get('rmq','cidr_max_length'))
            self.cidr_batch_count=int(config.get('rmq','cidr_batch_count'))
            self.ipv4_max_length=int(config.get('rmq','ipv4_max_length'))
            self.ipv4_batch_count=int(config.get('rmq','ipv4_batch_count'))
            self.db_host=config.get('mongo','host')
            self.db_port=int(config.get('mongo','port'))
            self.col_taskinfo=config.get('mongo','taskinfo_col_name')
            self.db_cidr=config.get('mongo','cidr_db_name')
            self.db_ipv4=config.get('mongo','ipv4_db_name')
        except Exception,e:
            print u'reading config.ini error!',repr(e)
            sys.exit(0)
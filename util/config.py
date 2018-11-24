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
            self.cidr_send_channel=config.get('rmq','cidr_send_channel')
            self.plugin_send_channel=config.get('rmq','plugin_send_channel')
            self.cidr_receive_channel=config.get('rmq','cidr_receive_channel')
            self.plugin_receive_channel=config.get('rmq','plugin_receive_channel')
            self.cidr_max_length=int(config.get('rmq','cidr_max_length'))
            self.cidr_batch_count=int(config.get('rmq','cidr_batch_count'))
            self.plugin_max_length=int(config.get('rmq','plugin_max_length'))
            self.plugin_batch_count=int(config.get('rmq','plugin_batch_count'))
            self.db_host=config.get('mongo','host')
            self.db_port=int(config.get('mongo','port'))
            self.col_taskinfo=config.get('mongo','taskinfo_col_name')
            self.db_cidr=config.get('mongo','cidr_db_name')
            self.db_plugin=config.get('mongo','plugin_db_name')
        except Exception,e:
            print u'reading config.ini error!',repr(e)
            sys.exit(0)

# coding=utf-8
from ssh import SSHConnection
import sys
if len(sys.argv)!=2:
    print ('sys args wrong!')
    sys.exit(0)
iplist=['118.184.81.44','118.184.81.46','154.223.179.148','154.223.175.59']
for ip in iplist:
    con=SSHConnection(ip,22,'root',sys.argv[1])
    con.exec_command('apt install python-pip -y')
    con.exec_command('pip install pika')
    con.exec_command('pip install logging')

print ('---start install erlang---')
con.exec_command('apt install erlang -y')
print ('---end install erlang---')
print ('---start install rmqserver---')
con.exec_command('apt install rabbitmq-server -y')
con.exec_command('rabbitmq-plugins enable rabbitmq_management')
# user=input('please input rmqserver user:')
# passwd=input('please input password:')
user='worker'
passwd='hello'
con.exec_command('rabbitmqctl add_user %s %s' % (user,passwd))
con.exec_command('rabbitmqctl set_user_tags %s administrator' % (user))
con.exec_command('rabbitmqctl set_permissions -p / %s \'.*\' \'.*\' \'.*\'' % (user))

print ('---end install rmqserver---')

con.close()
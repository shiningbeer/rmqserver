# coding=utf-8
from ssh import SSHConnection
import sys
if len(sys.argv)!=2:
    print ('sys args wrong!')
    sys.exit(0)
host='154.223.179.149'
con=SSHConnection(host,22,'root',sys.argv[1])
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
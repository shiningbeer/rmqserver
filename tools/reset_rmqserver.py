
# coding=utf-8
from ssh import SSHConnection
import sys
if len(sys.argv)!=3:
    print ('sys args wrong!')
    sys.exit(0)
con=SSHConnection(sys.argv[1],22,'root',sys.argv[2])
user=input('please input rmqserver user:')
passwd=input('please input password:')
con.exec_command('rabbitmqctl stop_app')
con.exec_command('rabbitmqctl reset')
con.exec_command('rabbitmqctl start_app')
con.exec_command('rabbitmqctl add_user %s %s' % (user,passwd))
con.exec_command('rabbitmqctl set_user_tags %s administrator' % (user))
con.exec_command('rabbitmqctl set_permissions -p / %s \'.*\' \'.*\' \'.*\'' % (user))

con.close()
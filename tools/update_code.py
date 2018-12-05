
# coding=utf-8
from ssh import SSHConnection
from threading import Thread
import sys
sys.path.append('..')
from util.functions import is_ipv4
if len(sys.argv)!=2:
    print ('sys args wrong!')
    sys.exit(0)

try:
    f=open('iplist.txt','r')
except Exception as e:
    print (repr(e))
    sys.exit(0)

passwd=sys.argv[1]

def install_simple_node(ip,passwd):
    con=SSHConnection(ip,22,'root',passwd)
    con.exec_command('apt install python-pip -y')
    con.exec_command('pip install pika')
    con.exec_command('pip install Ipy')
    con.exec_command('pip install requests')
    con.exec_command('pip install chardet')

line_number=0
for line in f:
    line_number+=1
    if not is_ipv4(line):
        print(('file contains none-ipv4 format at line : %s' % line_number))
        sys.exit(0)
# everything is ok, add the task to db
f.seek(0)
total=line_number
for line in f:
    line=line.strip()
    Thread(target=install_simple_node,args=(line,passwd)).start()
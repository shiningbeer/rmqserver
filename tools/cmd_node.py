
# coding=utf-8
from ssh import SSHConnection
from threading import Thread
import sys
sys.path.append('..')
from util.functions import is_ipv4

# args number is 2
if len(sys.argv)!=3:
    print ('sys args wrong!')
    sys.exit(0)
passwd=sys.argv[2]
cmd_file=sys.argv[1]

# open the files
try:
    f=open('iplist.txt','r')
    f_cmd=open(cmd_file,'r')
except Exception as e:
    print (repr(e))
    sys.exit(0)

# is the lines of iplist file are all ipv4 formats?
line_number=0
for line in f:
    line_number+=1
    if not is_ipv4(line):
        print(('file contains none-ipv4 format at line : %s' % line_number))
        sys.exit(0)
# thread func to execute the command on the vps
def install_simple_node(ip,passwd, cmd_list):
    con=SSHConnection(ip,22,'root',passwd)
    for cmd in cmd_list:
        con.exec_command(cmd)
    con.close()
# take out the cmds to a list
cmd_list=[]
for line in f_cmd:
    line=line.strip()
    cmd_list.append(line)

f.seek(0)
for line in f:
    line=line.strip()
    Thread(target=install_simple_node,args=(line,passwd,cmd_list)).start()
f.close()
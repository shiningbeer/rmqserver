一、部署环境
1、安装python3,pip3
2、pip3 install pika,paramiko,Ipy,termColor

二、部署
1、执行tools目录下install_rmqserver.py，在指定vps上安装rmqserver
2、在iplist文件下填入节点vps的ip列表，执行insall_node install password,  其中install为要在vps上执行的命令的记录文件， password为这些vps统一的密码
3、可登录rmqserver的ip地址 xxx.xxx.xxx.xxx:15672查看server的工作情况和node上worker的连接详情

三、运行服务
1、执行src目录下run.py，持续打印任务发布信息和任务进展信息，该程序监视是否有任务状态，一旦有任务需要执行将立即向rqmserver派发任务
2、执行src目录下result_listen.py，不加参数默认开启一个线程监听cidr任务，两个线程监听ipv4任务， -c x 指定cidr开启x个，-i x 指定ipv4开启x个

四、任务命令
Src目录下，add, del,pause, resume, 参数查看代码

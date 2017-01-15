#!/bin/bash


for((i=0;i<4;++i));do
    echo "start process $i" 
    python receive.py &
done
echo "=============="
sleep 1

# 因为查询rabbitmq的队列需要root权限
sudo echo -e  "send 10 oranges ...\n=============="
python send.py


sleep 21
ps -ef|grep receive.py | grep -v grep|cut -c 10-14|xargs kill


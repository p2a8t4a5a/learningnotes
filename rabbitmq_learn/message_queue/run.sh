#!/bin/bash

# 因为查询rabbitmq的队列需要root权限
sudo echo -e  "send 10 apples ...\n=============="
python send.py

for((i=0;i<4;++i));do
    echo "start process $i" 
    python receive.py $i &
done
echo "=============="

# kill all when queue is empty
while [ 0 != $(sudo rabbitmqctl list_queues|grep food_queue|cut -c 12) ];do 
    sleep 1
done
# ps -ef|grep receive.py|grep -v grep|cut -c 10-14|xargs kill
sudo pkill -f "python receive.py"

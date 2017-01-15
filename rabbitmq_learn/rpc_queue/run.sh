#!/bin/bash






echo "start server"
python server.py &
sleep 1
echo "start client"
python client.py &

sleep 20
ps -ef|grep "python server.py"|grep -v grep|cut -c 10-14|xargs kill
ps -ef|grep "python client.py"|grep -v grep|cut -c 10-14|xargs kill

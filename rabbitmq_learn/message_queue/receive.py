#! /usr/bin/env python
# -*- coding:utf8 -*-
import time
import pika
import sys


def call_back(ch, method, properties, body):
    print "process: %d  message: %s"%(num,body)
    time.sleep(5)
    # 设置确认收到，防止意外退出,可以交给别的进程处理
    ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__=="__main__":
    global num
    if sys.argv[1:]:
        num = int(sys.argv[1])

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # 在send.py 中已经声明过，但用户可能不知道先运行send还是receive，所以为了安全再次声明一次
    channel.queue_declare("food_queue", durable=True)

    # 默认采用的是均分的策略，现在改成一个进程只分配一个任务,做完再分配
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(call_back, queue='food_queue',)

    # 开始死循环的执行任务
    channel.start_consuming()


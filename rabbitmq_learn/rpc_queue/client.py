# -*- coding:utf-8 -*-
import pika
import random
import time
import sys













def call_back(ch, method, props, body):
    print "\nresponse value",body
    ch.basic_ack(delivery_tag = method.delivery_tag)
    global has_ans
    has_ans=True


if __name__=="__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare("rpc_queue",durable=True)
    temp_queue = channel.queue_declare(exclusive=True)

    # 定义接收函数
    channel.basic_consume(call_back, queue=temp_queue.method.queue, no_ack=True)

    # 发出请求
    channel.basic_publish(exchange='', routing_key="rpc_queue", body=str(9),
        properties=pika.BasicProperties(delivery_mode=2, reply_to=temp_queue.method.queue))
    
    while True:
        connection.process_data_events()
        time.sleep(1)
        print ".",
        sys.stdout.flush()



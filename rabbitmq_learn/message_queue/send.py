#! /usr/bin/env python
# -*- coding:utf8 -*-
import pika



if __name__=="__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # 声明一个队列,并持久化(存在硬盘上) 可重复声明
    channel.queue_declare("food_queue", durable=True)
    
    for i in range(10):
        channel.basic_publish(exchange='',routing_key='food_queue', body='apple-'+str(i),
            properties=pika.BasicProperties(delivery_mode=2,))  # 消息持久化,必须这里和前面的durable都设置才有效
    connection.close()



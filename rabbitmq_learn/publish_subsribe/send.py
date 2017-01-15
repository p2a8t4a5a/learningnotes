# -*- coding:utf-8 -*-
import pika
import random





def fanout_method():
    # 向所有队列广播
    channel.exchange_declare("logs", type='fanout')

    for i in range(10):
        channel.basic_publish(exchange='logs',routing_key="",body='orange'+str(i),
            properties=pika.BasicProperties(delivery_mode=2,)) # persistent message

def direct_method():
    # 向指定key广播
    channel.exchange_declare("direct_logs", type='direct')

    severities = ["warning","info","error"]
    for i in range(10):
        severity = random.choice(severities)
        print severity,'orange'+str(i)
        channel.basic_publish(exchange='direct_logs', routing_key=severity, body='orange'+str(i),
            properties=pika.BasicProperties(delivery_mode=2,)) # persistent message
    print "="*20

def topic_method():
    # 向指定多值key广播
    channel.exchange_declare("topic_logs", type='topic')
    colors = ["red","blue"]
    fruits = ["apple","banana"]
    size = ["big","small"]
    for i in range(10):
        severity = random.choice(colors)+"."+random.choice(fruits)+"."+random.choice(size)
        print severity,str(i)
        channel.basic_publish(exchange='topic_logs', routing_key=severity, body=str(i),
            properties=pika.BasicProperties(delivery_mode=2,)) # persistent message
    print "="*20


if __name__=="__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # fanout_method()
    # direct_method()
    topic_method()
    connection.close()


# -*- coding:utf-8 -*-
import time
import pika



def call_back(ch, method, properties, body):
    print "message:",body
    time.sleep(10)
    ch.basic_ack(delivery_tag = method.delivery_tag)


def fanout_method():
    """ 全部广播 """
    channel.exchange_declare("logs", type='fanout')
    # 新建一个临时队列 设置自动删除
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange="logs", queue=queue_name)

    channel.basic_consume(call_back, queue=queue_name)
    channel.basic_qos(prefetch_count=1)
    channel.start_consuming()


def direct_method():
    """ 指定的字段 """
    channel.exchange_declare("direct_logs", type='direct')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    for temp in ["warning","info"]:
        channel.queue_bind(exchange="direct_logs", routing_key=temp, queue=queue_name)

    channel.basic_consume(call_back, queue=queue_name)
    channel.basic_qos(prefetch_count=1)
    channel.start_consuming()

def topic_method():
    """ 多个字段 """
    channel.exchange_declare("topic_logs", type='topic')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    for temp in ["red.*.big","blue.#"]:
        channel.queue_bind(exchange="topic_logs", routing_key=temp, queue=queue_name)

    channel.basic_consume(call_back, queue=queue_name)
    channel.basic_qos(prefetch_count=1)
    channel.start_consuming()


if __name__=="__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    # fanout_method()
    # direct_method()
    topic_method()
    connection.close()


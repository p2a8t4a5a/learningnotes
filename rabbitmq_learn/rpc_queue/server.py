# -*- coding:utf-8 -*-
import time
import pika









def on_request(ch, method, props, body):
    n = int(body)

    response = n*n
    time.sleep(10)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
if __name__=="__main__":
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue="rpc_queue",durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue="rpc_queue")
    channel.start_consuming()
    connection.close()
    

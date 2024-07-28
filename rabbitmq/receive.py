import functools
import time

import pika
from pika import spec
from pika.adapters.blocking_connection import BlockingChannel

connection = pika.BlockingConnection(pika.connection.ConnectionParameters(host='1781833300178911.mq-amqp.cn-hangzhou-a.aliyuncs.com',port=5672, virtual_host='yibms', credentials=pika.credentials.PlainCredentials(
                                                                              'MjoxNzgxODMzMzAwMTc4OTExOkxUQUk1dEI5ZFptV1pQd2dwYzFMcXcxZA==',
                                                                              'NzBGQjgzMjgxQzQyMEQ3OThDNDE4QjgzRUY2RjlEODBGOTgwNDAyOToxNzEzOTI1ODg2MTc5'
                                                                          )))
channel = connection.channel()

# channel.queue_declare(queue='dev_task')


def callback(ch: BlockingChannel, method: spec.Basic.Deliver, properties: spec.BasicProperties, body: bytes):
    connection.add_callback_threadsafe(functools.partial(do_work, (ch, method, properties, body)))


def do_work(ch: BlockingChannel, method: spec.Basic.Deliver, properties: spec.BasicProperties, body: bytes):
    try:
        print(f'[x] received {body.decode()}')
        time.sleep(20)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f'[ack] received {body.decode()}')
    except Exception as e:
        print(e)
    finally:
        print(ch.connection.is_open)
        # ch.basic_ack(delivery_tag=method.delivery_tag)


# auto_ack=False 代表消息不自动确认
channel.basic_consume(on_message_callback=do_work, queue='dev_task', auto_ack=False)

channel.start_consuming()

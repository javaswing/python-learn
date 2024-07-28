import pika

connection = pika.BlockingConnection(pika.connection.ConnectionParameters(host='localhost',
                                                                          port=5672,
                                                                          virtual_host='/',
                                                                          credentials=pika.credentials.PlainCredentials(
                                                                              'guest',
                                                                              'guest'
                                                                          )))
properties = pika.BasicProperties(message_id='hellow')

channel = connection.channel()

channel.queue_declare(queue='hello')

msg = '你好，我是来自hello队列的消息'

channel.basic_publish(exchange='', routing_key='hello', body=msg.encode('utf-8'), properties=properties)

print(f"[x] send '{msg}'")
connection.close()

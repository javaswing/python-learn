
# https://www.alibabacloud.com/help/zh/apsaramq-for-rabbitmq/use-cases/automatic-recovery-from-network-failures#0a88a08a3eubs
import logging

import pika
from pika import BaseConnection
from pika.channel import Channel

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


class Consumer(object):

    def __init__(self, amp_url, queue):
        self.should_reconnect = False

        self._connection: BaseConnection | None = None
        self._channel: Channel | None = None
        self._closing = False
        self.url = amp_url

        self._queue = queue

    def connect(self):
        """
        创建 connection,并设置回调
        """
        return pika.SelectConnection(
            parameters=pika.URLParameters(self.url),
            on_open_callback=self.on_connection_open,
            on_open_error_callback=self.on_connection_open_failed,
            on_close_callback=self.on_channel_closed
        )

    def on_connection_open(self, _unused_connection):
        """
        连接成功的回调
        """
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_connection_open_failed(self, _unused_connection: BaseConnection, err):
        """
        创建连接错误的回调
        """
        LOGGER.error("Connection failed: %s", err)
        self.reconnect()

    def reconnect(self):
        """
        重连，修改 should_reconnect为 True，并停止 io_loop
        """
        self.should_reconnect = True,
        self.stop()

    def on_channel_open(self, channel: Channel):
        """
        创建 channel 之后的回调
        """
        self._channel = channel
        self._channel.add_on_close_callback(self.on_channel_closed)
        self.start_consuming()

    def on_channel_closed(self, channel, reason):
        """
        channel 关闭的回调
        """
        LOGGER.warning('Channel %i was closed: %s', channel, reason)
        self.close_connection()

    def start_consuming(self):
        """
        开始消费
        """
        LOGGER.info('start consuming...')
        self._channel.basic_consume(queue=self._queue, on_message_callback=self.on_message, auto_ack=False)

    def close_connection(self):
        """
        关闭连接
        """
        if self._connection.is_closing or self._connection.is_closed:
            LOGGER.info('Connection is closing or already closed')
        else:
            LOGGER.info('Closing connection')
            self._connection.close()

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        """
        消费消息并上传 ack
        """
        LOGGER.info('Received message %s', body.decode())
        self._channel.basic_ack(delivery_tag=basic_deliver.delivery_tag)

    def run(self):
        """
        创建 connection，并启动 io_loop
        """
        self._connection = self.connect()
        self._connection.ioloop.start()

    def stop(self):
        """
        停止 io_loop
        """
        if not self._closing:
            self._closing = True
            self._connection.ioloop.stop()
            LOGGER.info('Stopping ioloop')

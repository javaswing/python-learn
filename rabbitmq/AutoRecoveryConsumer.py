import time

from rabbitmq.consumer import Consumer


class AutoRecoveryConsumer(object):

    def __init__(self, amqp_url, queue):
        self._amqp_url = amqp_url
        self._queue = queue
        self._consumer = Consumer(self._amqp_url, queue)

    def run(self):
        while True:
            try:
                self._consumer.run()
            except KeyboardInterrupt:
                self._consumer.stop()
                break
            self.maybe_reconnect()

    def maybe_reconnect(self):
        if self._consumer.should_reconnect:
            self._consumer.stop()
            time.sleep(1)
            self._consumer = Consumer(self._amqp_url, self._queue)


def main():
    username = 'guest'
    password = 'guest'
    host = 'localhost'
    port = 5672
    vhost = ''
    queue = 'hello'
    amqp_url = 'amqp://{}:{}@{}:{}/{}'.format(username, password, host, port, vhost)
    consumer = AutoRecoveryConsumer(amqp_url, queue)
    consumer.run()


if __name__ == '__main__':
    main()

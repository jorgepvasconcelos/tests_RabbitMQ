import pika
from pika.exchange_type import ExchangeType


class Consumer1:
    def __init__(self):
        self.EXCHANGE_NAME = 'direct_logs'
        self.EXCHANGE_TYPE = ExchangeType.direct
        self.BINDING_KEY = 'info1'
        self.QUEUE_NAME = ''

        self.connection = None
        self.channel = None
        self.exchange = None
        self.queue = None

    def run(self):
        self.create_connection()
        self.create_channel()
        self.declare_exchange()
        self.declare_queue()
        self.declare_queue_bind()
        self.declare_consume()
        self.start_consuming()

    def create_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    def create_channel(self):
        self.channel = self.connection.channel()

    def declare_exchange(self):
        self.exchange = self.channel.exchange_declare(exchange=self.EXCHANGE_NAME, exchange_type=self.EXCHANGE_TYPE)

    def declare_queue(self):
        self.queue = self.channel.queue_declare(queue=self.QUEUE_NAME, exclusive=True)
        self.QUEUE_NAME = self.queue.method.queue

    def declare_queue_bind(self):
        self.channel.queue_bind(exchange=self.EXCHANGE_NAME, queue=self.QUEUE_NAME, routing_key=self.BINDING_KEY)

    def declare_consume(self):
        self.channel.basic_consume(queue=self.QUEUE_NAME, on_message_callback=self.callback, auto_ack=True)

    def start_consuming(self):
        print(f'INICIADO: {self.__class__.__name__}')

        self.channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        print(body.decode())


if __name__ == '__main__':
    try:
        Consumer1().run()
    except Exception as e:
        print(e)

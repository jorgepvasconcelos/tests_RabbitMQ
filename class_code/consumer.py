import pika


class Consumer:
    def __init__(self):
        self.exchange_name = 'direct_logs'
        self.binding_key = 'info'

        self.connection = None
        self.channel = None
        self.exchange = None
        self.queue = None
        self.queue_name = None

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
        self.exchange = self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')

    def declare_queue(self):
        self.queue = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = self.queue.method.queue

    def declare_queue_bind(self):
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key=self.binding_key)

    def declare_consume(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

    def start_consuming(self):
        print(f'INICIADO: {self.__class__.__name__}')

        self.channel.start_consuming()

    @staticmethod
    def callback(ch, method, properties, body):
        print(body.decode())


if __name__ == '__main__':
    try:
        Consumer().run()
    except Exception as e:
        print(e)

import pika


class Producer:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.exchange = None

    def run(self):
        self.create_connection()
        self.create_channel()
        self.declare_exchange()

        binding_key = 'info1'
        body = 'isso e uma info'
        self.publish_message(binding_key=binding_key, body=body)

        self.connection.close()

    def create_connection(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    def create_channel(self):
        self.channel = self.connection.channel()

    def declare_exchange(self):
        self.exchange = self.channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    def publish_message(self, binding_key, body):
        self.channel.basic_publish(
            exchange='direct_logs',
            routing_key=binding_key,
            body=body)


if __name__ == '__main__':
    try:
        Producer().run()
    except Exception as e:
        print(e)

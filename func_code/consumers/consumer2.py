import pika
from pika.exchange_type import ExchangeType

from func_code.connection import get_connection


def callback(ch, method, properties, body):
    print(body.decode())


def consumer2():
    CONSUMER_NAME = 'consumer2'

    EXCHANGE_NAME = 'direct_logs'
    EXCHANGE_TYPE = ExchangeType.direct
    BINDING_KEY = 'info2'
    QUEUE_NAME = ''

    connection = get_connection()

    channel = connection.channel()

    exchange = channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type=EXCHANGE_TYPE)

    queue = channel.queue_declare(queue=QUEUE_NAME, exclusive=True)
    QUEUE_NAME = queue.method.queue

    channel.queue_bind(exchange=EXCHANGE_NAME, queue=QUEUE_NAME, routing_key=BINDING_KEY)

    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

    print(f'INICIADO: {CONSUMER_NAME}')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        consumer2()
    except Exception as e:
        print(e)

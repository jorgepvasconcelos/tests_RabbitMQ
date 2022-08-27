import pika
from pika.exchange_type import ExchangeType


def producer1():
    producer_name = 'producer1'

    exchange_name = 'direct_logs'
    exchange_type = ExchangeType.direct
    binding_key = 'info1'

    body = b'isso e uma info 1'

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    exchange = channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type)

    channel.basic_publish(
        exchange='direct_logs',
        routing_key=binding_key,
        body=body)

    print(f'{producer_name} send a message')


if __name__ == '__main__':
    try:
        producer1()
    except Exception as e:
        print(e)

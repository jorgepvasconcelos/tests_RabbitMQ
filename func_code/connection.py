import time

import pika


def get_connection():

    host = 'service_rabbitmq'
    # host = 'localhost'
    port = 5672

    # connection = pika.BlockingConnection(pika.URLParameters(f"amqp://guest:guest@{host}:{port}/"))

    credentials = pika.credentials.PlainCredentials(username="guest", password="guest")
    parameters = pika.ConnectionParameters(
        host=host,
        port=port,
        credentials=credentials,
        heartbeat=10,
    )

    connection = pika.BlockingConnection(parameters=parameters)
    return connection

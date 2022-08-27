#!/usr/bin/env python
import pika, sys, os

from body_validator import validate_body2 as validate_body
from body_validator import RequestExpected


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    @validate_body(RequestExpected)
    def callback(ch, method, properties, body: RequestExpected):
        print(f" [x] Received: {body.value}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

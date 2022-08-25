#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')


message = json.dumps({'value': 10})

channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent 'Hello World!'")
connection.close()

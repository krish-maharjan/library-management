from django.core.management.base import BaseCommand
import pika
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # Declare the exchange, routingkey and queue
        exchange_name = 'borrow'
        routing_key = 'borrowroute'
        queue_name = 'bookmgmt'

        # exchange, routingkey and queue
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
        channel.queue_declare(queue=queue_name)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

        def callback(ch, method, properties, body):
            message = json.loads(body)
            print(f"Received message: {message}")

        channel.basic_consume(queue="bookmgmt", on_message_callback=callback, auto_ack=True)

        print("Waiting for message")

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            connection.close()
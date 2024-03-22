import pika
import json

class ProducerRequest:
    def __init__(self):
        self.connection_parameters = pika.ConnectionParameters('localhost')
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()

    def produce(self, get_exchange_name, get_routing_key, get_message):
        self.channel.queue_declare(queue='bookmgmt')

        # Message content
        message = {"token": get_message}

        self.channel.basic_publish(exchange=get_exchange_name, routing_key=get_routing_key, body=json.dumps(message))

        print(f"Sent message: {message}")

        self.connection.close()

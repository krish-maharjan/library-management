import uuid
import pika
import json

class ProducerRequest:
    def __init__(self, host='localhost'):
        self.connection_parameters = pika.ConnectionParameters(host)
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.response = None
        self.correlation_id = None
        self.callback_queue = None
        self.setup_callback_queue()

    def setup_callback_queue(self):
        result = self.channel.queue_declare(queue='bookmgmtq')
        self.callback_queue = result.method.queue
        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            self.response = body

    def produce(self, get_exchange_name, get_routing_key, get_message):
        try:
            self.response = None
            self.correlation_id = str(uuid.uuid4())

            # Message content
            message = {"book_id": get_message}

            self.channel.basic_publish(
                exchange=get_exchange_name,
                routing_key=get_routing_key,
                properties=pika.BasicProperties(
                    reply_to=self.callback_queue,
                    correlation_id=self.correlation_id,
                ),
                body=json.dumps(message)
            )

            print(f"Sent message: {message}")

            while self.response is None:
                self.connection.process_data_events()
            return self.response.decode('utf-8')
        finally:
            self.connection.close()
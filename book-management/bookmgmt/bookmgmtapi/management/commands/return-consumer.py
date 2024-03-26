from django.core.management.base import BaseCommand
import pika
import json
from bookmgmtapi.models import BooksMgmtModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        exchange_name = 'bookqtyex'
        routing_key = 'bootqtyrt'
        queue_name = 'bookmgmtq'

        # exchange, routingkey and queue
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
        channel.queue_declare(queue=queue_name)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

        def callback(ch, method, properties, body):
            data = json.loads(body)
            bookid = data.get('book_id')
            response = "Book not found."

            try:
                book = BooksMgmtModel.objects.get(book_id=bookid)
                response = book.quantity

                book.quantity = book.quantity + 1
                book.save()

            except BooksMgmtModel.DoesNotExist:
                pass

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

        print("Waiting for message")

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            connection.close()
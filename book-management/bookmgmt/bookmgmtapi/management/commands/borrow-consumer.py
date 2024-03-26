from django.core.management.base import BaseCommand
import pika
import json
from bookmgmtapi.models import BooksMgmtModel

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # Declare the exchange, routingkey and queue
        exchange_name = 'bookborrowex'
        routing_key = 'bookborrowrt'
        queue_name = 'bookmgmtq'

        # exchange, routingkey and queue
        channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
        channel.queue_declare(queue=queue_name)
        channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

        def callback(ch, method, properties, body):
            data = json.loads(body)
            bookid = data.get('book_id')
            # print('bookid', bookid)
            response = "Book not found."

            try:
                book = BooksMgmtModel.objects.get(book_id=bookid)
                response = book.availability_status

                if (response == 'True'):
                    if book.quantity > 0:
                        book.quantity = book.quantity - 1
                        book.save()
                        print('book', book.quantity)

            except BooksMgmtModel.DoesNotExist:
                pass

            # Sending the response back to the reply_to queue
            ch.basic_publish(
                exchange='',
                routing_key=properties.reply_to,
                properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                body=str(response)
            )
            ch.basic_ack(delivery_tag=method.delivery_tag)

        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)

        print("Waiting for message")

        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            connection.close()
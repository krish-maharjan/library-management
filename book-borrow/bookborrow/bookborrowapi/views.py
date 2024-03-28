from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .serializers import BookBorrowSerializer
from .producer import ProducerRequest
from .models import BorrowBookModel

# Create your views here.
class BorrowView(APIView):
    def post(self, request, format=None):
        received_request = json.loads(request.body)
        borrow_serializer = BookBorrowSerializer(data=received_request)

        if (borrow_serializer.is_valid()):
            bookid = borrow_serializer.validated_data.get('book_id', None)
            producer = ProducerRequest()
            producer_response = producer.produce('bookborrowex', 'bookborrowrt', bookid)
            print('producer_response', producer_response)

            if (producer_response=="False"):
                return Response({"msg": "Book not available"}, status=status.HTTP_404_NOT_FOUND)

            borrow_serializer.save()
            return Response({"msg": borrow_serializer.data, "availability": producer_response}, status=status.HTTP_201_CREATED)
        else:
            return Response(borrow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnView(APIView):
    def post(self, request, format=None):
        received_request = json.loads(request.body)

        bookid = received_request.get('book_id')
        borrowid = int(received_request.get('borrow_id'))
        return_date = received_request.get('submitted_date')

        print("borrowid", borrowid, type(borrowid))

        BookModel = BorrowBookModel.objects.get(borrow_id=borrowid)
        BookModel.submitted_date = return_date
        BookModel.save()

        producer = ProducerRequest()
        producer_request = producer.produce('bookqtyex', 'bootqtyrt', bookid)

        return Response({"msg": "suscess"}, status=status.HTTP_200_OK)

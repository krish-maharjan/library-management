from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .serializers import BookBorrowSerializer

# Create your views here.
class BorrowView(APIView):
    def post(self, request, format=None):
        received_request = json.loads(request.body)
        borrow_serializer = BookBorrowSerializer(data=received_request)
        if (borrow_serializer.is_valid()):
            borrow_serializer.save()
            return Response({"msg": borrow_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(borrow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnView(APIView):
    def post(self, request, format=None):
        received_request = json.loads(request.body)
        print(received_request)
        borrow_serializer = BookBorrowSerializer(data=received_request)
        if (borrow_serializer.is_valid()):
            print(borrow_serializer.data)
            return Response({"msg": "suscess"}, status=status.HTTP_201_CREATED)
        else:
            return Response(borrow_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
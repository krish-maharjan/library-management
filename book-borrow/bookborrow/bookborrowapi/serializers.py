from rest_framework import serializers
from .models import BorrowBookModel

class BookBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowBookModel
        fields = '__all__'
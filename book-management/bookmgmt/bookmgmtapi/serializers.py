from rest_framework import serializers
from .models import BooksMgmtModel

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksMgmtModel
        fields = '__all__'
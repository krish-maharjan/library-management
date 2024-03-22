import uuid

from django.db import models

# Create your models here.
class BooksMgmtModel(models.Model):
    book_id = models.UUIDField(editable=False, primary_key=False, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    availability_status = models.CharField(max_length=255)

    def __str__(self):
        return self.title
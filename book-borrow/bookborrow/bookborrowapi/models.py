import uuid

from django.db import models

# Create your models here.
class BorrowBookModel(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    book_id = models.IntegerField()
    borrowing_date = models.DateField()
    due_date = models.DateField()
    submitted_date = models.DateField(null=True)
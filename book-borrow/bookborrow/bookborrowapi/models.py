import uuid

from django.db import models

# Create your models here.
class BorrowBookModel(models.Model):
    borrow_id = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    borrowing_date = models.DateField()
    due_date = models.DateField()
    submitted_date = models.DateField(null=True)
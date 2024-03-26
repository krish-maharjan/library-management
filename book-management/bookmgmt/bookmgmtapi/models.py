from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class BooksMgmtModel(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    availability_status = models.CharField(max_length=255, default=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def save(self, *args, **kwargs):
        if self.quantity < 1:
            self.availability_status = False
        if self.quantity > 0:
            self.availability_status = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
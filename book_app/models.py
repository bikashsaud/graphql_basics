from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    edition = models.IntegerField()

    def __str__(self):
        return str(self.book_name)

        
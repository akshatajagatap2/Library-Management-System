from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=200, null=True)
    author_name = models.CharField(max_length=200, null=True)
    publication = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.book_name

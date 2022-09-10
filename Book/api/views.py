from rest_framework import viewsets
from Book.models import Book
from Book.api.serializers import BookSerializer


class BookCRUD(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
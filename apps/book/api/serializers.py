from rest_framework import serializers
from apps.book.models import BookList, Book
from apps.users.api.serializers import CustomUserSerializer


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListDetailSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = BookList
        fields = '__all__'

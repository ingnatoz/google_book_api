import requests
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from apps.book.models import BookList, Book
from .serializers import *


class BookListViewSets(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    model = BookList
    serializer_class = BookListSerializer
    list_serializer_class = BookListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        book_lists = self.get_queryset()
        book_list_serializer = self.list_serializer_class(book_lists, many=True)
        return Response(book_list_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        book_list_serializer = self.serializer_class(data=request.data)
        if book_list_serializer.is_valid():
            book_list_serializer.save()
            return Response({
                'message': 'Book list registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': book_list_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book_list = self.get_object(pk)
        book_list_serializer = self.serializer_class(book_list)
        return Response(book_list_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book_list = self.get_object(pk)
        book_list_serializer = self.serializer_class(book_list, data=request.data)
        if book_list_serializer.is_valid():
            book_list_serializer.save()
            return Response({
                'message': 'Book list updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': book_list_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book_list_destroy = self.model.objects.filter(id=pk)
        if len(book_list_destroy) == 1:
            book_list_destroy.delete()
            return Response({
                'message': 'Book list deleted successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The Book list you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"])
    def get_book_list_detail_by_id(self, request, ):
        print(request.data['book_list_id'])
        book_list = self.model.objects.filter(id=request.data['book_list_id']).first()
        book_list_serializer = BookListDetailSerializer(book_list)
        return Response(book_list_serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def get_book_list_by_user_id(self, request, ):
        book_lists = self.model.objects.filter(user_id=request.data['user_id']).all()
        if len(book_lists) >= 1:
            print(len(book_lists))
            book_list_serializer = self.list_serializer_class(book_lists, many=True)
            return Response({
                'message': 'Book list.',
                'book_list_by_user_id': book_list_serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'User has no book list'
        }, status=status.HTTP_404_NOT_FOUND)


class BookViewSets(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    model = Book
    serializer_class = BookSerializer
    list_serializer_class = BookSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def list(self, request):
        books = self.get_queryset()
        books_serializer = self.list_serializer_class(books, many=True)
        return Response(books_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        book_serializer = self.serializer_class(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response({
                'message': 'Book list registered successfully.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry.',
            'errors': book_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        book = self.get_object(pk)
        book_serializer = self.serializer_class(book)
        return Response(book_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        book = self.get_object(pk)
        book_serializer = self.serializer_class(book, data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response({
                'message': 'Book list updated successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update.',
            'errors': book_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        book_destroy = self.model.objects.filter(id=pk)
        if len(book_destroy) == 1:
            book_destroy.delete()
            return Response({
                'message': 'Book list deleted successfully.'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'The Book list you want to remove does not exist.'
        }, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["post"])
    def get_book_by_google(self, request, ):
        url = 'https://www.googleapis.com/books/v1/volumes?q=' + request.data['search_terms']
        response = requests.get(url, headers={})
        if response.status_code == 200:
            return Response({
                'message': response.json()
            }, status=status.HTTP_200_OK)

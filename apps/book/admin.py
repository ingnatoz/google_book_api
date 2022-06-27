from django.contrib import admin
from .models import *


@admin.register(BookList)
class BookList(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'user', 'created_at', 'updated_at',)
    ordering = ('id',)
    search_fields = ('id', 'category_name', 'user', 'created_at', 'updated_at',)
    list_editable = ('category_name', 'user',)
    list_display_links = ('id',)
    list_filter = ('category_name', 'user', 'created_at', 'updated_at',)
    list_per_page = 100


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'editorial', 'book_list', 'created_at', 'updated_at',)
    ordering = ('id',)
    search_fields = ('id', 'title', 'author', 'editorial', 'book_list', 'created_at', 'updated_at',)
    list_editable = ('title', 'author', 'editorial', 'book_list',)
    list_display_links = ('id',)
    list_filter = ('title', 'author', 'editorial', 'book_list', 'created_at', 'updated_at',)
    list_per_page = 100

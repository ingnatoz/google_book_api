from django.db import models
from apps.users.models import User


class BookList(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(User, null=False, related_name='user_book_list', on_delete=models.RESTRICT,
                             verbose_name='UserBookList')
    created_at = models.DateTimeField('Created at', auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField('Updated at', auto_now=True, null=True, editable=False)

    def book_list_format(self):
        return "{} / {}".format(self.id, self.category_name)

    def __str__(self):
        return self.book_list_format()

    class Meta:
        verbose_name = 'Book List'
        verbose_name_plural = 'BookLists'
        db_table = 'book_list'
        ordering = ['id']


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=False, unique=True)
    author = models.CharField(max_length=150, null=False, )
    editorial = models.CharField(max_length=150, null=False, )
    google_book_id = models.CharField(max_length=500, null=False, unique=True, blank=True)
    book_list = models.ForeignKey(BookList, null=False, related_name='book_list', on_delete=models.CASCADE,
                                  verbose_name='Book_List')
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False, )
    updated_at = models.DateTimeField(auto_now=True, null=True, editable=False, )

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        db_table = 'book'
        ordering = ['id']

    def book_format(self):
        return "{} / {}".format(self.id, self.title)

    def __str__(self):
        return self.book_format()

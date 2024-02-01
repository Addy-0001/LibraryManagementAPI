from django.contrib import admin
from .models import Book, BookDetail, BorrowedBooks
# Register your models here.

admin.site.register(Book)
admin.site.register(BookDetail)
admin.site.register(BorrowedBooks)
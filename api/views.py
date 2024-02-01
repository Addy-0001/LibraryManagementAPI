from django.shortcuts import render
from .serializers import UserModelSerializer, BookModelSerializer, BookDetailModelSerializer, BorrowedBooksModelSerializer
from user.models import UserModel
from books.models import Book, BookDetail, BorrowedBooks
# Create your views here.

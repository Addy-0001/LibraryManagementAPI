from django.shortcuts import render
from .serializers import UserModelSerializer, BookModelSerializer, BookDetailModelSerializer, BorrowedBooksModelSerializer
from user.models import UserModel
from books.models import Book, BookDetail, BorrowedBooks
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class UserListView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


@api_view()
def UserDetailView(request, ID):
    queryset = UserModel.objects.get(UserID=ID)
    return Response({
        'UserID': queryset.UserID,
        'Name': queryset.Name,
        'Email': queryset.Email,
        'MembershipDate': queryset.MembershipDate
    })


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book
    serializer_class = BookModelSerializer


@api_view(['GET'])
def BookDetailView(request, ID):
    queryset = Book.objects.get(BookID=ID)
    return Response({
        'BookID': queryset.BookID,
        "Title": queryset.Title,
        "ISBN": queryset.ISBN,
        "Genre": queryset.Genre,
        "PublishedDate": queryset.PublishedDate,
    })


class CreateBookDetail(CreateAPIView):
    queryset = BookDetail.objects.all()
    serializer_class = BookDetailModelSerializer


class BookDetailRetriveUpdateDestroy(RetrieveUpdateAPIView):
    queryset = BookDetail.objects.all()
    lookup_url_kwarg = 'BookID'
    serializer_class = BookDetailModelSerializer


class BorrowBookView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksModelSerializer


class ReturnBookView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksModelSerializer
    lookup_url_kwarg = 'BookID'


class ListBurrowedBooks(ListAPIView):
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksModelSerializer

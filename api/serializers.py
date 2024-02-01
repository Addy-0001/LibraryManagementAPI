from user.models import UserModel
from books.models import Book, BookDetail, BorrowedBooks
from rest_framework.serializers import ModelSerializer

class UserModelSerializer(ModelSerializer):
    model = UserModel
    fields = "__all__"

class BookModelSerializer(ModelSerializer):
    model = Book
    fields = "__all__"

class BookDetailModelSerializer(ModelSerializer):
    model = BookDetail
    fields = "__all__"

class BorrowedBooksModelSerializer(ModelSerializer):
    model = BorrowedBooks
    fields = "__all__"
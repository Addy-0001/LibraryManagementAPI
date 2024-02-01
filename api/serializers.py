from user.models import UserModel
from books.models import Book, BookDetail, BorrowedBooks
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookDetailModelSerializer(ModelSerializer):
    class Meta:
        model = BookDetail
        fields = "__all__"


class BorrowedBooksModelSerializer(ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = "__all__"

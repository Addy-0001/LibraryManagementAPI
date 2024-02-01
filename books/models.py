from django.db import models
from user.models import UserModel
# Create your models here.
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)
    ISBN = models.CharField(max_length=200)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.Title} ({self.BookID})"


class BookDetail(models.Model):
    DetailID = models.AutoField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete = models.CASCADE)
    NumberofPages = models.IntegerField()
    Publisher = models.CharField(max_length=500)
    Language = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.BookID}"

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField()

    def __str__(self):
        return f"{self.UserID} ({self.BookID})"


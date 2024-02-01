from django.urls import path
from . import views
urlpatterns = [
    path('list-users/', views.UserListView.as_view(), name="list-users"),
    path('create-users/', views.UserCreateView.as_view(), name='create-users'),
    path('user/<int:ID>/', views.UserDetailView, name='user-detail-view'),
    path('list-books/', views.BookListView.as_view(), name="list-books"),
    path('create-books/', views.BookCreateView.as_view(), name='create-books'),
    path('book-detail/<int:ID>/', views.BookDetailView, name='book-detail-view'),
    path('book-detail-update/<int:BookID>/',
         views.BookDetailRetriveUpdateDestroy.as_view(), name="book-detail-update"),
    path('create-book-detail/', views.CreateBookDetail.as_view(),
         name='create-book-detail'),
    path('borrow-book/', views.BorrowBookView.as_view(), name = 'borrow-book'),
    path('return-book/<int:BookID>/',
         views.ReturnBookView.as_view(), name='return-book'),
    path('list-borrowed-books/', views.ListBurrowedBooks.as_view(),
         name='list-borrowed-books'),
]

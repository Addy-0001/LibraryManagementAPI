from django.urls import path, include
from . import views
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.SignupView, name='signup'),
    path('logout-page/', views.logout_page, name='logout-page'),
    path('logged-out/', views.logged_out, name='logged-out'),
    path('logged-in/', views.LoggedInView.as_view(), name='logged-in')
]

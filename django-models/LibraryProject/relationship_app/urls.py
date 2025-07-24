from django.urls import path
from . import views
from .views import list_books

#Configure URL Patterns:
urlpatterns = [
    path('books/', views.list_books, name='book'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
]

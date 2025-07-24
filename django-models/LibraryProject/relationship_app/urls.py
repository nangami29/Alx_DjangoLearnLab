from django.urls import path
from . import views

#Configure URL Patterns:
urlpatterns = [
    path('books/', views.book_list, name='book'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
]

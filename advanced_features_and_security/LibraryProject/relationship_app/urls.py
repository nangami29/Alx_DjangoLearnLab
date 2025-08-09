from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


#Configure URL Patterns:
urlpatterns = [
    path('books/', views.list_books, name='book'),
    path('library/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin_view', views.admin_view, name='admin'),
    path('librarian-view', views.librarian_view, name='librarian'),
    path('Member', views.member_view, name='member'),
     path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]

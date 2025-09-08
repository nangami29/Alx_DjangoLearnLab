from django.urls import path
from . import views
from .views import FeedView
urlpatterns = [
  
   
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

   
    # Comment URLs
    path('posts/<int:post_id>/comments/', views.CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),

     path('feed/', FeedView.as_view(), name='feed'),
]

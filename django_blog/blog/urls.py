from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import SignUpView 
from . import views

from .views import (
    PostListView, PostDetailView, PostCreateView,PostUpdateView, PostDeleteView, CommentListView, CommentDeleteView, CommentCreateView,  CommentUpdateView)
from .views import  posts_by_tag, search_posts

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('profile/', LogoutView.as_view(template_name='registration/profile.html'), name='profile'),
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path("register/", views.register_view, name="register"),
    path("profile/", views.profile_view, name="profile"),
    path('posts/', PostListView.as_view(), name='post-list'), 
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'), 
     path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),   
  

       #comment
    path('post/<int:pk>/comments', CommentListView.as_view(), name='comment_list'),
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
     path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
      path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),

   
    path('search/', search_posts, name='search_posts'),
    path('tag/<str:tag_name>/', posts_by_tag, name='posts_by_tag'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts_by_tag'),
]

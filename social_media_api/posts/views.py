from django.shortcuts import render
from rest_framework import generics, viewsets, serializers, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly, IsAuthenticated
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

# Create your views here.
class PostListView(generics.ListAPIView):
    queryset =Post.objects.all()
    serializer_class =PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_backends= [filters.SearchFilter]
    search_fields = ['title', 'content', 'author']
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering_fields = ['title', 'author']
    ordering = ['title']

# create post

# Create a new post
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Retrieve a single post
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Update a post
class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

# Delete a post
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


# Comment Views


# List all comments for a specific post
class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'author__username']
    ordering = ['created_at']

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__username']
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'author__username']
    ordering = ['title']

    def perform_create(self, serializer):
        # Assign the logged-in user as the post author
        serializer.save(author=self.request.user)

# Create a new comment for a specific post
class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(post=get_object_or_404(Post, id=post_id), author=self.request.user)

# Retrieve a single comment
class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Update a comment
class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

# Delete a comment
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at', 'author__username']
    ordering = ['created_at']

    def get_queryset(self):
        # List comments for a specific post if post_id is in URL
        post_id = self.kwargs.get('post_pk')
        if post_id:
            return Comment.objects.filter(post__id=post_id)
        return Comment.objects.all()
    
    
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_pk')
        serializer.save(post=Post.objects.get(id=post_id), author=self.request.user)











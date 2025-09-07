from django.shortcuts import render
from rest_framework import generics, filters, permissions, serializers
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from  django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends= [filters.SearchFilter]
    search_fields = ['title', 'publication_year', 'author']
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book
class BookCreateView(LoginRequiredMixin, generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom validation: no future publication years
        pub_year = self.request.data.get('publication_year')
        if pub_year and int(pub_year) > datetime.now().year:
            raise serializers.ValidationError(
                {"publication_year": "Publication year cannot be in the future."}
            )
        # Save book with logged-in user as author if needed
        serializer.save()

# RetrieveView: Get a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends= [filters.SearchFilter]
    search_fields = ['title', 'publication_year', 'author']
    permission_classes = [IsAuthenticatedOrReadOnly]


# UpdateView: Update a book by ID
class BookUpdateView(LoginRequiredMixin, generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Extra validation before saving
        pub_year = self.request.data.get('publication_year')
        if pub_year and int(pub_year) > datetime.now().year:
            raise serializers.ValidationError(
                {"publication_year": "Publication year cannot be in the future."}
            )
        serializer.save()

# DeleteView: Delete a book by ID
class BookDeleteView(LoginRequiredMixin, generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]



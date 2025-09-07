from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create a test book
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2020
        )

        self.client = APIClient()
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book.pk})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book.pk})

    def test_list_books(self):
        """Test retrieving the list of books (readable by anyone)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Test Book", str(response.data))

    def test_retrieve_book_detail(self):
        """Test retrieving a single book detail."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book_authenticated(self):
        """Test creating a book when logged in."""
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "New Book", "author": "Jane Smith", "publication_year": 2021}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """Test creating a book without login should fail."""
        data = {"title": "New Book", "author": "Jane Smith", "publication_year": 2021}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book when logged in."""
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Updated Book", "author": "John Doe", "publication_year": 2022}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book when logged in."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        """Test filtering books by author."""
        response = self.client.get(f"{self.list_url}?author=John")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("John Doe", str(response.data))

    def test_order_books(self):
        """Test ordering books by publication_year."""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

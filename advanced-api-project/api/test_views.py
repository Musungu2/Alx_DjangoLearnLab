from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.admin = User.objects.create_superuser(username="admin", password="adminpass")

        # Create authors and books
        self.author1 = Author.objects.create(name="Author One")
        self.author2 = Author.objects.create(name="Author Two")

        self.book1 = Book.objects.create(title="Book One", author=self.author1, publication_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author=self.author2, publication_year=2010)

        # Endpoints
        self.list_url = reverse("book-list")  # adjust to your URL name
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    def test_list_books_public(self):
        """Anyone can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book_public(self):
        """Anyone can retrieve a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_authenticated(self):
        """Only authenticated users can create books"""
        self.client.login(username="testuser", password="pass1234")
        data = {
            "title": "New Book",
            "author": self.author1.id,
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create books"""
        data = {
            "title": "Fail Book",
            "author": self.author1.id,
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_admin_only(self):
        """Only admins can update books"""
        self.client.login(username="admin", password="adminpass")
        data = {"title": "Updated Book", "author": self.author1.id, "publication_year": 2005}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_admin_only(self):
        """Only admins can delete books"""
        self.client.login(username="admin", password="adminpass")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Filter books by author name"""
        response = self.client.get(f"{self.list_url}?author__name=Author One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books_by_title(self):
        """Search for a book by title"""
        response = self.client.get(f"{self.list_url}?search=Book Two")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_order_books_by_publication_year(self):
        """Order books by publication_year ascending"""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")

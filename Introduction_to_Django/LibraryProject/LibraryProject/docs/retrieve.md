# Retrieve the Book Instance

To retrieve the book instance we created earlier, we use the `.get()` method from Django's ORM.

```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(title="The Alchemist")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

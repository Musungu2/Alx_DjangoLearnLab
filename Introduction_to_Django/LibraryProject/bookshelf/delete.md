# Delete the Book Instance

To delete the book instance from the database, retrieve it and call the `.delete()` method.

```python
from bookshelf.models import Book

book_to_delete = Book.objects.get(title="The Alchemist")
book_to_delete.delete()
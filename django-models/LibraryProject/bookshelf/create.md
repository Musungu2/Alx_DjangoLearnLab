# Create a Book Instance

I create a `Book` instance by importing the model and calling the `.create()` method:

```python
from bookshelf.models import Book

Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)


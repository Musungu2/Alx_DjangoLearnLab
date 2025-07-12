# Update the Book Title

To update the title of the book from "1984" to "Nineteen Eighty-Four", retrieve the instance, modify the field, and save it:

```python
retrieved_book = Book.objects.get(title="1984")
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)

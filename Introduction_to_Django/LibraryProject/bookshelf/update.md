# Update the Book Title

To update the title of the book from "The Alchemist" to "The Alchemist: A Fable About Following Your Dream", retrieve the instance, modify the field, and save it:

```python
retrieved_book = Book.objects.get(title="The Alchemist")
retrieved_book.title = "The Alchemist: A Fable About Following Your Dream"
retrieved_book.save()
print(retrieved_book.title)

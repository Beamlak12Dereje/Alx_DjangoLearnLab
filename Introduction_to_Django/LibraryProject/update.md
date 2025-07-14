# Update Operation

```python
from bookshelf.models import Book

# Find the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book)

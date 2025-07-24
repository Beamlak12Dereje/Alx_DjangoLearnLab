# Delete Operation

```python
from bookshelf.models import Book

# Find and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check remaining books
print(Book.objects.all())

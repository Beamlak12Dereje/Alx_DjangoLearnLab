# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve and display all Book instances
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)

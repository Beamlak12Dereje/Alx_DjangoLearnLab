# Create Operation

```python
from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve and display all Book instances
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Update Operation

```python
from bookshelf.models import Book

# Find the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book)
# Delete Operation

```python
from bookshelf.models import Book

# Find and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Check remaining books
print(Book.objects.all())

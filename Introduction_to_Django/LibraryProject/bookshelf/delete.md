# ✅ Import the model first
from bookshelf.models import Book

# ✅ Create a book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print("Book created:", book)

# ✅ Retrieve the book
retrieved_book = Book.objects.get(title="1984")
print("Book retrieved:", retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)

# ✅ Update the title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print("Book updated title:", retrieved_book.title)

# ✅ Delete the book
retrieved_book.delete()
print("Book deleted.")

# ✅ Confirm deletion
books = Book.objects.all()
print("Remaining books:", list(books))

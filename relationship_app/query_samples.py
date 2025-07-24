import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author (assume author with id=1)
    author_books = Book.objects.filter(author_id=1)
    print("Books by Author 1:")
    for book in author_books:
        print(f"- {book.title}")

    # List all books in a library (assume library with id=1)
    library = Library.objects.get(id=1)
    print(f"\nBooks in Library '{library.name}':")
    for book in library.books.all():
        print(f"- {book.title}")

    # Retrieve the librarian for a library (assume library with id=1)
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian of '{library.name}': {librarian.name}")

if __name__ == "__main__":
    run_queries()

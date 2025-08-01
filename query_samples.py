from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Query all books by a specific author
    author_name = 'Author Name Here'
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

    # List all books in a library
    library_name = 'Library Name Here'
    try:
        library = Library.objects.get(name=library_name)
        print(f"\nBooks in library {library_name}:")
        for book in library.books.all():
            print(f"- {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

    # Retrieve the librarian for a library
    try:
        librarian = Librarian.objects.get(library__name=library_name)
        print(f"\nLibrarian of library {library_name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library {library_name}")

if __name__ == "__main__":
    run_queries()

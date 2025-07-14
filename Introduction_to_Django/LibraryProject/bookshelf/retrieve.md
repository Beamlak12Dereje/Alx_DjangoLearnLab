# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")
print(book)
# Expected output: Book object (1)

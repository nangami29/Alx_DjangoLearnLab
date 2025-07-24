from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Jane Austen"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author) 
    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# 2. List all books in a specific library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# 3. Retrieve the librarian for a library
try:
    library = Librarian.objects.get(library=library_name)
    librarian = library.librarian
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

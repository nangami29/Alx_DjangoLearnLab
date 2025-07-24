from relationship_app.models import Author, Book, Library

#Query all books by a specific author.
books=Book.objects.prefetch_related('title')

#List all books in a library.
library=Library.objects.filter('library')

#Retrieve the librarian for a library

library = Library.objects.get('library')
    
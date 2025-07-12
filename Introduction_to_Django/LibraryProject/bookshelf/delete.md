from bookshelf.models import Book
retrieved_book.delete()
print(Book.objects.all())
# <QuerySet [<Book: Book object (2)>]>

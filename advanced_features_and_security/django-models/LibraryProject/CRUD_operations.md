# create 

In [6]: from bookshelf.models import Book
   ...:
   ...: book= Book.objects.create(
   ...:     title="1984",
   ...:     author="George Orwell",
   ...:     publication_year = 1949
   ...:
   ...: )
   ...: print(book)
   ...:
Book object (2)

In [7]: book.save()
 # retrieve
 
In [9]: retrieved_book=Book.objects.get(id=book.id)
   ...: print (retrieved_book.title)
1984
 # update






  from bookshelf.models import Book
   ...:    ...:
   ...:    ...: book= Book.objects.create(
   ...:    ...:     title="1984",
   ...:    ...:     author="George Orwell",
   ...:    ...:     publication_year = 1949
   ...:    ...:
   ...:    ...: )
   ...:    ...: print(book)
   ...:
Book object (3)

In [3]: book.save()

In [4]: retrieved_book=Book.objects.get(id=book.id)^M
   ...:    ...: print (retrieved_book.title)^M
   ...:
1984

In [5]: retrieved_book.title = "Nineteen Eighty-Four"^M
   ...: retrieved_book.save()^M
   ...: print(retrieved_book.title)
Nineteen Eighty-Four

In [6]: retrieved_book.delete()
   ...: print(Book.objects.all())
   ...:
<QuerySet [<Book: Book object (2)>]>

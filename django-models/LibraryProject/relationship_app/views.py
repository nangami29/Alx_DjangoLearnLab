from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Library
from django.views.generic.detail import DetailView
# Create your views here.
#Implement Function-based View:
def book_list(request):
    author_name='kev'
    try:
        author = Author.objects.get(name=author_name)
        books =Book.objects.all()
 
    except Author.DoesNotExist:
        books = []
    context={'book_list':books,
             }
    return render(request, 'relationship_app/list_books.html', context)

#Implement Class-based View:
from .models import Library
class LibraryDetailView(DetailView):
    model=Library
    template_name='relationship_app/library_detail.html'
    context_object_name='library'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add related books to the context
        context['book_list'] = self.object.books.all()
        return context
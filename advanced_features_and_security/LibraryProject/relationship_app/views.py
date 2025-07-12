from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Library
from django.views.generic.detail import DetailView
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
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
    

  #Setup User Authentication Views:
class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='register.html'  

    #Set Up Role-Based Views
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'admin'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'member'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'member'

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')


#Update Views to Enforce Permissions
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
       
        pass
    else:
        
        pass
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
   
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    
    return render(request, 'relationship_app/delete_book.html')

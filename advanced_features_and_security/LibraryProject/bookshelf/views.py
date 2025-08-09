from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@permission_required('app_name.can_create', raise_exception=True)
def book_create(request):
    # Example only — form handling omitted
    return HttpResponse("Book created (dummy response)")

@permission_required('app_name.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # Example only — form handling omitted
    return HttpResponse(f"Book '{book.title}' edited (dummy response)")

@permission_required('app_name.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return HttpResponse("Book deleted")

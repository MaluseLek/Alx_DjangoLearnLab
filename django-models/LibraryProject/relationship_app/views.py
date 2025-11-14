from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-based view to display a list of books in the database
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/book_list.html', context)


# Class-based view to display a list of books in the database
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Prefetch related books to reduce DB queries
    def get_queryset(self):
        return Library.objects.prefetch_related('books')
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test, permission_required
from functools import wraps
from django.core.exceptions import PermissionDenied



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
    

# Add Register your views in urls.py to make them accessible via URLs.
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')


# Role-based access control decorator
def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'userprofile'):
                user_role = request.user.userprofile.role
                if user_role in allowed_roles:
                    return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped_view
    return decorator


# Views with role-based access control
@role_required(['Admin'])
def admin_dashboard(request):
    return render(request, 'relationship_app/admin_dashboard.html')

@role_required(['Librarian'])
def librarian_dashboard(request):
    return render(request, 'relationship_app/librarian_dashboard.html')

@role_required(['Member', 'Librarian', 'Admin'])
def member_dashboard(request):
    return render(request, 'relationship_app/member_dashboard.html')


# Update Views to Enforce Permissions
@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('book_list')
        else:
            error = "Both title and author are required."
            return render(request, 'relationship_app/book_form.html', {'error': error})
        
    return render(request, 'relationship_app/book_form.html')

@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            book.title = title
            book.author = author
            book.save()
            return redirect('book_list')
        else:
            error = "Both title and author are required."
            return render(request, 'relationship_app/book_form.html', {'book': book, 'error': error})
        
    return render(request, 'relationship_app/book_form.html', {'book': book})


@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import RegisterView
from .views.admin_view import admin_dashboard
from .views.librarian_view import librarian_dashboard
from .views.member_view import member_dashboard

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('books/add/', views.add_book, name='add-book'),
    path('books/<int:book_id>/edit/', views.edit_book, name='edit-book'),
    path('books/<int:book_id>/delete/', views.delete_book, name='delete-book'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]

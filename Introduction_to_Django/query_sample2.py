# relationship_app/query_samples.py

import os
import django

# 1️⃣ Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

print("=== Django ORM Query Samples ===\n")

# 2️⃣ Query all books by a specific author
author_name = "J.K. Rowling"
books_by_author = Book.objects.filter(author__name=author_name)

if books_by_author.exists():
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f" - {book.title}")
else:
    print(f"No books found for author '{author_name}'.")
print("\n" + "-"*40 + "\n")


# 3️⃣ List all books in a specific library
library_name = "Central Library"
books_in_library = Book.objects.filter(library__name=library_name)

if books_in_library.exists():
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(f" - {book.title}")
else:
    print(f"No books found in library '{library_name}'.")
print("\n" + "-"*40 + "\n")


# 4️⃣ Retrieve the librarian for a specific library
try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian for {library_name}: {librarian.name}")
except ObjectDoesNotExist:
    print(f"No librarian found for '{library_name}'.")
except MultipleObjectsReturned:
    print(f"Multiple librarians found for '{library_name}'. Check your data!")

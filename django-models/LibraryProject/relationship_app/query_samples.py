import os
import sys
import django

# absolute path to the project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Query all books by a specific author
author_name = "George Orwell"
try:
    # First, get the specific author object
    author = Author.objects.get(name=author_name)
    # Then, find all books by that author. This is more direct than a reverse lookup.
    books_by_author = Book.objects.filter(author=author)

    if books_by_author.exists():
        print(f"Books by {author.name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No books found by {author.name}.")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")
print("\n" + "-"*40 + "\n")


# List all books in a library
library_name = "City Library"
try:
    # First, get the specific library object
    library = Library.objects.get(name=library_name)
    # Then, get all books related to that library
    library_books = library.books.all()
    if library_books.exists():
        print(f"\nBooks in {library.name}:")
        for book in library_books:
            print(f"- {book.title} by {book.author.name}")
    else:
        print(f"No books found in {library.name}.")
except Library.DoesNotExist:
    print(f"The library '{library_name}' was not found.")
print("\n" + "-"*40 + "\n")


# Retrieve the librarian for a library
try:
    # First, get the library object. We can reuse library_name from above.
    library = Library.objects.get(name=library_name)
    # Then, get the librarian associated with that library object.
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"The library '{library_name}' was not found.")
except Librarian.DoesNotExist:
    print(f"No librarian found for {library_name}.")
print("\n" + "-"*40 + "\n")

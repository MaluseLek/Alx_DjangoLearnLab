# Delete the Book instance

>>> from bookshelf.models import Book
>>> book.delete()
OUTPUT: (1, {'bookshelf.Book': 1})
>>> Book.objects.all()

<!-- OUTPUT: <QuerySet []> --!>

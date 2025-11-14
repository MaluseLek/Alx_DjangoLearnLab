# Database CRUD Operations

<!-- Creating Books in Django Shell -->
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()

<!-- Retrieve and display all attributes of the book -->
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

<!-- Update the title of “1984” to “Nineteen Eighty-Four” -->
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)
< Nineteen Eighty-Four

<!-- Delete the Book instance -->
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>

<!-- Creating Books in Django Shell -->
>>> from bookshelf.models import Book
<!-- -->
<!-- Create Multiple Books — Basic Method (One by One) -->
>>> Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> Book.objects.create(title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960)
>>> Book.objects.create(title="Pride and Prejudice", author="Jane Austen", publication_year=1813)
<!-- -->
<!-- Create Multiple Books at Once — Using bulk_create() -->
>>> books = [
    Book(title="The Hobbit", author="J.R.R. Tolkien", publication_year=1937),
    Book(title="The Catcher in the Rye", author="J.D. Salinger", publication_year=1951),
    Book(title="The Alchemist", author="Paulo Coelho", publication_year=1988),
    Book(title="Beloved", author="Toni Morrison", publication_year=1987)
]
>>> Book.objects.bulk_create(books)
<QuerySet [<Book: The Hobbit>, <Book: The Catcher in the Rye>, <Book: The Alchemist>, <Book: Beloved>]>

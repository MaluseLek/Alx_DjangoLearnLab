from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_editable = ('publication_year',)
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'publication_year')
        }),
    )
    ordering = ('title',)
    list_per_page = 10


# Manual registration line (Optionally Use Decorator-Based Registration)
admin.site.register(Book, BookAdmin)


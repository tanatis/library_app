from django.contrib import admin

from library_app.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author', 'genre', 'number_of_pages']
    list_filter = ['author', 'genre']

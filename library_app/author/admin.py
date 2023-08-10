from django.contrib import admin

from library_app.author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'nationality', 'birth_year', 'death_year']
    list_filter = ['nationality']

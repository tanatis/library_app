from django.contrib import admin

from library_app.borrow.models import Borrow


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ['user', 'get_book_title', 'return_date']
    list_filter = ['book__title']

    @staticmethod
    def get_book_title(obj):
        return obj.book.title

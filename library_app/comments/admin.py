from django.contrib import admin

from library_app.comments.models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    search_fields = ['to_book__title']
    list_display = ['content', 'get_book_title', 'get_username']
    list_filter = ['to_book__title']

    @staticmethod
    def get_book_title(obj):
        return obj.to_book.title

    @staticmethod
    def get_username(obj):
        return obj.user if obj.user else 'DELETED USER'

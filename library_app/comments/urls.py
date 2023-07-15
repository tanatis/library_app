from django.urls import path

from library_app.comments.views import comment_add

urlpatterns = [
    path('<int:book_id>/', comment_add, name='add comment'),
]

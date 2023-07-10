from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from library_app.book.views import list_books, book_add, book_edit, book_details

urlpatterns = [
    path('', list_books, name='all books'),
    path('add/', book_add, name='add books'),
    path('<int:pk>/', book_details, name='details books'),
    path('<int:pk>/edit/', book_edit, name='edit books'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
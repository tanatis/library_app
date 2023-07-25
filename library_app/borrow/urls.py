from django.urls import path

from library_app.borrow.views import borrow_book, borrow_list, borrow_delete, send_email_reminder

urlpatterns = [
    path('<int:book_pk>/', borrow_book, name='borrow book'),
    path('list/', borrow_list, name='borrow list'),
    path('<int:pk>/delete/', borrow_delete, name='borrow delete'),
    path('<int:pk>/send/', send_email_reminder, name='borrow reminder'),
]

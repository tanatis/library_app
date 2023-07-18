from django.urls import path, include

from library_app.author.views import author_details, author_delete, author_edit, AuthorCreateView, list_authors

urlpatterns = [
    path('', list_authors, name='all authors'),
    path('create/', AuthorCreateView.as_view(), name='author create'),
    path('<int:pk>/', include([
        path('', author_details, name='author details'),
        path('edit/', author_edit, name='author edit'),
        path('delete/', author_delete, name='author delete'),
    ])),
]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('library_app.accounts.urls')),
    path('', include('library_app.common.urls')),
    path('authors/', include('library_app.author.urls')),
    path('books/', include('library_app.book.urls')),
    path('borrow/', include('library_app.borrow.urls')),
    path('comment/', include('library_app.comments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('library_app.accounts.urls')),
    path('', include('library_app.common.urls')),
]

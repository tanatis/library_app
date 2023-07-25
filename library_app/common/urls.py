from django.urls import path

from library_app.common.views import index, restricted, error_page

urlpatterns = [
    path('', index, name='index'),
    path('restricted/', restricted, name='restricted'),
    path('error/', error_page, name='error'),
]

from django.urls import path

from library_app.common.views import index, restricted

urlpatterns = [
    path('', index, name='index'),
    path('restricted/', restricted, name='restricted'),
]

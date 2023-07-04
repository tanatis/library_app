from django.urls import path

from library_app.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
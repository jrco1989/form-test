from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path(route = '',view = views.index, name='index'),
    path(route = 'new/', view = views.RegistryCreate.as_view(), name='new_record'),
]
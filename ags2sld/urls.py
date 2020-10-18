from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^getsld$', views.get_sld, name='get_sld'),
    re_path(r'^getmap', views.get_map, name='get_map'),
]
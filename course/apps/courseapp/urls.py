from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^update/(?P<id>\d+)$', views.update, name="update"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^comment/(?P<id>\d+)$', views.comment, name = 'comment'),
]

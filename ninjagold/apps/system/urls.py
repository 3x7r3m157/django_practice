from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^processfarm$', views.processfarm),
    url(r'^processcave$', views.processcave),
    url(r'^processhouse$', views.processhouse),
    url(r'^processcasino$', views.processcasino),


]

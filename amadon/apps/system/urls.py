from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^thankyou$', views.thankyou),
    url(r'^monkey$', views.monkey),
    url(r'^giraffe$', views.giraffe),
    url(r'^elephant$', views.elephant)

]

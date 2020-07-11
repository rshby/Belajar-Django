from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile),
    url(r'^$', views.index),
    url(r'^recent/$', views.recent),
]
#-*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

app_name = "doc_types"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
]

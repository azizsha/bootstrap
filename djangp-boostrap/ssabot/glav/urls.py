# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.generic import ListView,DetailView
from glav.models import bloggs
from . import views

urlpatterns = [
    url(r'^$', ListView.as_view(queryset = bloggs.objects.raw('SELECT * FROM glav_bloggs ORDER BY date desc  ')[:3], template_name='glav/ind.html')),
    url(r'^about$', views.posts, name='post'),
    url(r'^contact$',views.about, name='about'),
    url(r'^check_user_name/$', views.check_user_name, name='check_user_name'),


]

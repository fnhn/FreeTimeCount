from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'FreeTimeCount.views.index'),
    url(r'^date/', 'FreeTimeCount.views.date'),
    url(r'^member/', 'FreeTimeCount.views.member'),
    url(r'^distribute/', 'FreeTimeCount.views.distribute'),
    url(r'^insert/', 'FreeTimeCount.views.insert'),
]

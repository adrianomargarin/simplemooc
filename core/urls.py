# -*- coding: utf-8 -*-

from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'core.views.home', name='home'),
    url(r'^contato$', 'core.views.contact', name='contact'),
]
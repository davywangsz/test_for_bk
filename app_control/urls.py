# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'app_control.views',
    (r'^$', 'home'),
    (r'^switch_func/$', 'switch_func'),
    (r'^execute_func/$', 'execute_func'),
    (r'^check_failed/$', 'check_failed'),
)

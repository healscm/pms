#-*- coding: utf-8 -*-
'''
    Author: smallmi
    Blog: http://www.smallmi.com
'''
from __future__ import unicode_literals
from django.conf.urls import url
from content import views,api

urlpatterns = [
    # url(r'^login/$', associate_openid, name='associate_openid'),
    url(r'^list$', views.fms_list,name='fms_list'),
    url(r'^add$', views.fms_add,name='fms_add'),
    url(r'^edit$', views.fms_edit, name='fms_edit'),
    url(r'^detail/(?P<id>\d+)$', views.fms_detail,name='fms_detail'),
    url(r'^search$', api.fms_search,name='fms_search'),


]

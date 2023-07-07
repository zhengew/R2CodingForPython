# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/7/6 下午1:15

from django.urls import path
from app01 import views

urlpatterns = [
    path('', views.app01Index),
    path('myfilter/', views.app01myfilter),
    path('mytags/', views.app01mytags),
]
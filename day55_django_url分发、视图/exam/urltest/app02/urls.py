# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/7/2 14:35

from django.urls import path
from app02 import views

urlpatterns = [
    path('', views.app02_index),
]
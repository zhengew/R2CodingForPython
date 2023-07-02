# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/7/2 14:33

from django.urls import path
from app01 import views

urlpatterns = [
    path('', views.app01_index),
]

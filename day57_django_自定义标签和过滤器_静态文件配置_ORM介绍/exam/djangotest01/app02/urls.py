# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/7/7 21:28

from django.urls import path
from app02 import views

urlpatterns = [
    path('', views.app02Index),
]
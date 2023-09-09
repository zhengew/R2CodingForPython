# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: urls.py
# @datatime: 2023/9/7 23:22

from django.urls import path
from app01 import views

urlpatterns = [
    path('', views.App01Views.as_view(), name='app01'),
    # 文件上传
    path('upload/', views.App01Views.as_view(), name='upload'),
]
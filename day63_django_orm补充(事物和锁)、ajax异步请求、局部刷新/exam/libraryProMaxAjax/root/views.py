from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.urls import reverse # url反向解析
from django.utils.decorators import method_decorator # 装饰器
# Create your views here.

# CBV
class RootView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.path == '/':
            return render(request, 'login.html')

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.urls import reverse # 反向解析url
# Create your views here.

class RootApp(View):

    def dispatch(self, request, *args, **kwargs):
        ret = super(RootApp, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        if request.path == '/':
            return render(request, 'home.html')
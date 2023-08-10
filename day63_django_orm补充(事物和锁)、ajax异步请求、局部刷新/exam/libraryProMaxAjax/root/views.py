import json

from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.urls import reverse # url反向解析
from django.utils.decorators import method_decorator # 装饰器
from root import models
# Create your views here.

# CBV
class RootView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.path == '/':
            return render(request, 'login.html')
        elif request.path == '/books/':
            return render(request, 'home.html')

    def post(self, request, *args, **kwargs):
        if request.path == '/':
            loginName = request.POST.get('loginName')
            yn_exist = models.UserInfo.objects.filter(username=loginName).exists()
            if yn_exist:
                loginPwd = request.POST.get('loginPwd')
                pwd = models.UserInfo.objects.get(username=loginName).password
                if loginPwd == pwd:
                    data = {'RETCODE': '200', 'DATA': '/books/', 'RETMSG': 'SUCCESS'}
                elif loginPwd == '':
                    data = {'RETCODE': 'PASSWORD_IS_NULL_ERROR', 'RETMSG': '请输入密码'}
                else:
                    data = {'RETCODE': 'USERNAME_PASSWORD_ERROR', 'RETMSG': '用户名或密码错误'}
            elif loginName == '':
                data = {'RETCODE': 'USERNAME_IS_NULL_ERROR', 'RETMSG': '请输入用户名'}
            else:
                data = {'RETCODE': 'USERNAME_NOT_EXISTS_ERROR', 'RETMSG': '用户名或密码错误'}
            data = json.dumps(data)
            return HttpResponse(data)


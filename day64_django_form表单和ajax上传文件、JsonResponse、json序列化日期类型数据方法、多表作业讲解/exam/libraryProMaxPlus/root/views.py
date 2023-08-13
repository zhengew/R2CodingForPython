from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse # url 方向解析
from django.http import JsonResponse # json响应
from django.utils.decorators import method_decorator # 装饰器
from django.views import View
from root import models

# Create your views here.

class RootView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return render(request, 'login.html')
        elif request.path == '/showBooks/':
            return HttpResponse('200 ok')

    def post(self, request, *args, **kwargs):

        if request.path == '/':
            data = request.POST.dict()
            loginName = data['username']
            loginPwd = data['password']
            yn_exist = models.UserInfo.objects.filter(username=loginName).exists()
            if yn_exist:
                password = models.UserInfo.objects.get(username=loginName).password
                if password == loginPwd:
                    res = {'RETCODE': '200', 'DATA': '/showBooks/', 'RETMSG': 'SUCCESS'}
                elif loginPwd.strip() == '':
                    res = {'RETCODE': 'PASSWORD_IS_NULL_ERROR', 'DATA': '', 'RETMSG': '请输入密码'}
                else:
                    res = {'RETCODE': 'USERNAME_OR_PASSWORD_ERROR', 'DATA': '', 'RETMSG': '用户名或密码错误'}
            elif loginName.strip() == '':
                res = {'RETCODE': 'USERNAME_IS_NULL_ERROR', 'DATA': '', 'RETMSG': '请输入用户名'}
            else:
                res = {'RETCODE': 'USERNAME_OR_PASSWORD_ERROR', 'DATA': '', 'RETMSG': '用户名或密码错误'}

            return JsonResponse(res)

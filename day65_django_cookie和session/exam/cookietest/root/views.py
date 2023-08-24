import os

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.utils.decorators import method_decorator # 装饰器
from django.views import View
from django.conf import settings
from root import models

# Create your views here.

class RootView(View):

    def dispatch(self, request, *args, **kwargs):

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        if request.path == '/':
            return redirect('login')

        elif request.path == '/login/':
            return render(request, 'login.html')

    def post(self, request, *args, **kwargs):

        if request.path == '/login/':
            data = request.POST.dict()
            yn_exist_uname = models.UserInfo.objects.filter(username=data['username']).exists()
            if yn_exist_uname:
                pwd = models.UserInfo.objects.get(username=data['username']).password
                if pwd == data['password']:
                    ret = {'RETCODE': 200, "RETMSG": "SUCCESS"}
                else:
                    ret = {'RETCODE': 901, "RETMSG": "用户名或密码错误"}
            else:
                ret = {'RETCODE': 901, "RETMSG": "用户名或密码错误"}

            # 响应对象设置 Cookie
            res = JsonResponse(ret)
            if ret['RETCODE'] == 200:
                res.set_cookie('is_login', True, max_age=1800)

            return res

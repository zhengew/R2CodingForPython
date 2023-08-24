import json

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views import View
from root import models

# Create your views here.

# 登录
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
            print(data)
            loginName = data.get('username')
            loginPwd = data.get('password')
            yn_exist_loginName = models.UserInfo.objects.filter(username=loginName).exists()
            if yn_exist_loginName:
                pwd = models.UserInfo.objects.get(username=loginName).password
                if loginPwd == pwd:
                    ret = {"RETCODE": 200, "RETMSG": 'SUCCESS'}
                else:
                    ret = {"RETCODE": "USERNAME_OR_PASSWORD_ERROR", "RETMSG": json.dumps("用户名或密码错误")}
            else:
                ret = {"RETCODE": "USERNAME_OR_PASSWORD_ERROR", "RETMSG": json.dumps("用户名或密码错误")}

            # 登录校验通过，设置 Session
            if ret['RETCODE'] == 200:
                request.session['is_login'] = True
                request.session['username'] = loginName

            return JsonResponse({"RETCODE": 200, "RETMSG": 'SUCCESS'})